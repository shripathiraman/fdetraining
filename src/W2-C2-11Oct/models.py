from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class PaymentTracker(BaseModel):
    transaction_id: str
    transaction_date: Optional[datetime] = Field(default_factory=datetime.now)
    sender_name: Optional[str] = None
    receiver_name: Optional[str] = None
    amount: float
    payment_mode: Optional[str] = "GPay"
    status: Optional[str] = "SUCCESS"
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None


class PaymentTrackerUpdate(BaseModel):
    sender_name: Optional[str] = None
    receiver_name: Optional[str] = None
    amount: Optional[float] = None
    payment_mode: Optional[str] = None
    status: Optional[str] = None
    remarks: Optional[str] = None
