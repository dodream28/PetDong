from pydantic import BaseModel
from typing import Optional

class HealthRecord(BaseModel):
    pet_id: str
    heart_rate: int
    distance: float
    timestamp: str  # ISO8601 형식 권장 (실제 개발 시 datetime 변환 가능성 있음)
