from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.usecase.notification_usecase import NotificationUseCase
from app.adapters.http.schemas import (
    NotificationCreateSchema, 
    NotificationUpdateSchema, 
    NotificationResponseSchema # Импортируем схему ответа
)
from app.di import get_notification_usecase # DI

router = APIRouter(prefix="/notifications", tags=["Notifications (CRUD)"])

@router.get("/user/{user_id}", response_model=List[NotificationResponseSchema])
def get_by_user(
    user_id: str, 
    usecase: NotificationUseCase = Depends(get_notification_usecase)
):
    """Получить все уведомления конкретного пользователя"""
    return usecase.get_user_notifications(user_id)

@router.post("", response_model=NotificationResponseSchema)
def create_notification(
    item: NotificationCreateSchema,
    usecase: NotificationUseCase = Depends(get_notification_usecase)
):
    """Создать уведомление вручную"""
    return usecase.create_manual_notification(item)

@router.put("/{id}", response_model=NotificationResponseSchema)
def update_notification(
    id: str, 
    item: NotificationUpdateSchema,
    usecase: NotificationUseCase = Depends(get_notification_usecase)
):
    """Обновить уведомление"""
    updated = usecase.update_notification(id, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Notification not found")
    return updated

@router.delete("/{id}")
def delete_notification(
    id: str,
    usecase: NotificationUseCase = Depends(get_notification_usecase)
):
    """Удалить уведомление"""
    if not usecase.delete_notification(id):
        raise HTTPException(status_code=404, detail="Notification not found")
    return {"message": "Deleted"}