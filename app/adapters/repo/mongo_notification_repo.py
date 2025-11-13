from app.domain.repositories import INotificationRepository
from app.domain.entities import Notification
from app.infrastructure.db import db
from bson import ObjectId
from datetime import datetime
from typing import List, Optional, Dict, Any

def _notification_serializer(n: dict) -> Optional[Notification]:
    """
    Приватный сериализатор (из crud.py).
    Конвертирует документ MongoDB в доменную сущность Notification.
    """
    if not n:
        return None
    return Notification(
        id=str(n["_id"]),
        user_id=n["user_id"],
        message=n["message"],
        type=n.get("type", "system"),
        status=n.get("status", "sent"),
        timestamp=n.get("timestamp", datetime.utcnow())
    )

class MongoNotificationRepository(INotificationRepository):
    
    def get_by_id(self, notification_id: str) -> Optional[Notification]:
        """Реализация crud.get_notification"""
        try:
            n = db.notifications.find_one({"_id": ObjectId(notification_id)})
            return _notification_serializer(n)
        except Exception:
            return None

    def create(self, data: Dict[str, Any]) -> Notification:
        """Реализация crud.create_notification"""
        if "timestamp" not in data:
            data["timestamp"] = datetime.utcnow()
        
        result = db.notifications.insert_one(data)
        new_doc = db.notifications.find_one({"_id": result.inserted_id})
        return _notification_serializer(new_doc)

    def get_by_user_id(self, user_id: str) -> List[Notification]:
        """Реализация crud.get_user_notifications"""
        notifications = db.notifications.find({"user_id": user_id})
        return [_notification_serializer(n) for n in notifications if n]

    def update(self, notification_id: str, data: Dict[str, Any]) -> Optional[Notification]:
        """Реализация crud.update_notification"""
        try:
            db.notifications.update_one({"_id": ObjectId(notification_id)}, {"$set": data})
            return self.get_by_id(notification_id)
        except Exception:
            return None

    def delete(self, notification_id: str) -> bool:
        """Реализация crud.delete_notification"""
        try:
            result = db.notifications.delete_one({"_id": ObjectId(notification_id)})
            return result.deleted_count > 0
        except Exception:
            return False