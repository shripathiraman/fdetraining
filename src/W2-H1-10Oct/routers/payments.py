from fastapi import APIRouter, HTTPException
from models.payments import Payments
import services.payments as payment_service

router = APIRouter()

@router.get("/payments")
def get_payments():
    return payment_service.read_all_payments()


@router.post("/payments")
def create_payment(payment: Payments):
    return payment_service.create_payment(payment)


@router.put("/payments/{payment_id}")
def update_payment(payment_id: str, payment: Payments):
    updated_payment = payment_service.update_payment(payment_id, payment)
    if not updated_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return updated_payment


@router.delete("/payments/{payment_id}")
def delete_payment(payment_id: str):
    if not payment_service.delete_payment(payment_id):
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"message": "Payment deleted successfully"}


@router.get("/payments/{payment_id}")
def get_payment(payment_id: str):
    payment = payment_service.read_payment_by_id(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment