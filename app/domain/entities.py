from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Notification(BaseModel):
    id: str
    user_id: str
    message: str
    type: str
    status: str
    timestamp: datetime