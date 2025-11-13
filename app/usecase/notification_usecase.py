from app.domain.repositories import INotificationRepository
from app.adapters.http.schemas import NotificationCreateSchema, NotificationUpdateSchema
from app.domain.entities import Notification
from typing import List, Optional, Dict, Any
import logging # Import logging

# Get Logger
log = logging.getLogger(__name__)

class NotificationUseCase:
    """
    Coordinates business logic for notifications.
    """
    def __init__(self, repo: INotificationRepository):
        self.repo = repo
    
    # --- CRUD Logic ---
    
    def get_user_notifications(self, user_id: str) -> List[Notification]:
        return self.repo.get_by_user_id(user_id)
    
    def create_manual_notification(self, item: NotificationCreateSchema) -> Notification:
        notif = self.repo.create(item.model_dump())
        log.info(f"Manual notification created for user {item.user_id}")
        return notif
            
    def update_notification(self, notif_id: str, item: NotificationUpdateSchema) -> Optional[Notification]:
        update_data = item.model_dump(exclude_unset=True)
        if not update_data:
            return self.repo.get_by_id(notif_id)
        return self.repo.update(notif_id, update_data)
            
    def delete_notification(self, notif_id: str) -> bool:
        return self.repo.delete(notif_id)

    # --- System Notification Logic ---

    def _create_system_notification(self, user_id: str, message: str, type: str) -> Notification:
        data = {
            "user_id": user_id,
            "message": message,
            "type": type,
            "status": "sent"
        }
        notif = self.repo.create(data)
        log.info(f"System notification ({type}) created for user {user_id}")
        return notif

    def notify_low_health(self, user_id: str) -> Notification:
        return self._create_system_notification(
            user_id=user_id,
            message="Your pet is feeling unwell! Take care of it.",
            type="pet"
        )

    def notify_low_mood(self, user_id: str) -> Notification:
        return self._create_system_notification(
            user_id=user_id,
            message="Your pet is in a bad mood. Play with it.",
            type="pet"
        )

    def notify_task_completed(self, user_id: str) -> Notification:
        return self._create_system_notification(
            user_id=user_id,
            message="Great job! You completed a task!",
            type="task"
        )

    def notify_task_failed(self, user_id: str) -> Notification:
        return self._create_system_notification(
            user_id=user_id,
            message="Task failed. Try again!",
            type="task"
        )
