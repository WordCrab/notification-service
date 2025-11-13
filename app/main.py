from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.adapters.http import (
    notification_router, 
    system_notify_router, 
    health_router
)
import logging

# 1. Setup Logger
log = logging.getLogger(__name__)

app = FastAPI(title="Notification Service (Deploy Ready)")

# 2. Friendly Error Handlers
@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    log.warning(f"Business logic error: {exc}")
    return JSONResponse(
        status_code=400,
        content={"error_type": "BusinessLogicError", "message": str(exc)},
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    log.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"error_type": "InternalServerError", "message": "An internal server error occurred."},
    )

# 3. Include routers
app.include_router(health_router.router)
app.include_router(notification_router.router)
app.include_router(system_notify_router.router)

@app.get("/")
def root():
    return {"message": "Notification Service is running"}
