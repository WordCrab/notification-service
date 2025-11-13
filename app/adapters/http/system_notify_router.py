from fastapi import APIRouter, Depends
from app.usecase.notification_usecase import NotificationUseCase
from app.di import get_notification_usecase # DI

# Роутер для внутренних системных уведомлений
router = APIRouter(prefix="/notify", tags=["Internal Notifications"], include_in_schema=False)

@router.post("/pet-low-health/{user_id}")
def notify_pet_low_health(
    user_id: str,
    usecase: NotificationUseCase = Depends(get_notification_usecase)
):
    """уведомление от Pet Service: низкое здоровье"""
    usecase.notify_low_health(user_id)
    return {"message": "Low health notification saved"}

@router.post("/pet-low-mood/{user_id}")
def notify_pet_low_mood(
    user_id: str,
    usecase: NotificationUseCase = Depends(get_notification_usecase)
):
    """уведомление от Pet Service: плохое настроение"""
    usecase.notify_low_mood(user_id)
    return {"message": "Low mood notification saved"}

@router.post("/task-completed/{user_id}")
def notify_task_completed(
    user_id: str,
    usecase: NotificationUseCase = Depends(get_notification_usecase)
):
    """уведомление от Task Service: задание завершено"""
    usecase.notify_task_completed(user_id)
    return {"message": "Task completion notification saved"}

@router.post("/task-failed/{user_id}")
def notify_task_failed(
    user_id: str,
    usecase: NotificationUseCase = Depends(get_notification_usecase)
):
    """уведомление от Task Service: задание провалено"""
    usecase.notify_task_failed(user_id)
    return {"message": "Task failed notification saved"}