from pydantic import BaseModel
from typing import Optional
from datetime import datetime
# Мы импортируем доменную сущность и используем ее как схему ответа
from app.domain.entities import Notification as NotificationResponseSchema

class NotificationCreateSchema(BaseModel):
    """Схема для POST /notifications (взято из models.py)"""
    user_id: str
    message: str
    type: str  
    status: str = "sent"

class NotificationUpdateSchema(BaseModel):
    """Схема для PUT /notifications/{id} (все поля опциональны)"""
    user_id: Optional[str] = None
    message: Optional[str] = None
    type: Optional[str] = None
    status: Optional[str] = None