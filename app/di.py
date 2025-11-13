from functools import lru_cache
from fastapi import Depends
from app.domain.repositories import INotificationRepository
from app.adapters.repo.mongo_notification_repo import MongoNotificationRepository
from app.usecase.notification_usecase import NotificationUseCase

@lru_cache(maxsize=1)
def get_notification_repo() -> INotificationRepository:
    """Провайдер для репозитория (синглтон)."""
    return MongoNotificationRepository()

def get_notification_usecase(
    repo: INotificationRepository = Depends(get_notification_repo)
) -> NotificationUseCase:
    """
    Провайдер для UseCase.
    Автоматически внедряет 'get_notification_repo' в NotificationUseCase.
    """
    return NotificationUseCase(repo=repo)