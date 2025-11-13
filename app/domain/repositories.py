from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from app.domain.entities import Notification

class INotificationRepository(ABC):
    
    @abstractmethod
    def create(self, data: Dict[str, Any]) -> Notification:
        """Создает уведомление в БД."""
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: str) -> List[Notification]:
        """Получает все уведомления пользователя."""
        pass
    
    @abstractmethod
    def get_by_id(self, notification_id: str) -> Optional[Notification]:
        """Получает одно уведомление по ID."""
        pass

    @abstractmethod
    def update(self, notification_id: str, data: Dict[str, Any]) -> Optional[Notification]:
        """Обновляет уведомление."""
        pass

    @abstractmethod
    def delete(self, notification_id: str) -> bool:
        """Удаляет уведомление."""
        pass