from fastapi import FastAPI, HTTPException, status
from models import PaymentTracker, PaymentTrackerUpdate
import services

app = FastAPI(
    title="Payment Tracker API",
    description="FastAPI service connected to PostgreSQL fde_db for tracking payments",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Payment Tracker API is running",
        "docs_url": "/docs",
    }


# Add / Create payment record
@app.post("/payments", status_code=status.HTTP_201_CREATED)
def create_payment(payment: PaymentTracker):
    try:
        return services.add_payment_srv(payment)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to create payment: {str(e)}",
        )


# Get all payment records
@app.get("/payments")
def get_all_payments():
    return services.get_all_payments_srv()


# Get payment record by transaction ID
@app.get("/payments/{transaction_id}")
def get_payment(transaction_id: str):
    result = services.get_payment_srv(transaction_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Payment transaction '{transaction_id}' not found",
        )
    return result


# Update payment record
@app.put("/payments/{transaction_id}")
def update_payment(transaction_id: str, payment: PaymentTrackerUpdate):
    result = services.update_payment_srv(transaction_id, payment)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Payment transaction '{transaction_id}' not found",
        )
    return result


# Delete payment record
@app.delete("/payments/{transaction_id}")
def delete_payment(transaction_id: str):
    success = services.delete_payment_srv(transaction_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Payment transaction '{transaction_id}' not found",
        )
    return {"message": f"Payment transaction '{transaction_id}' deleted successfully"}
