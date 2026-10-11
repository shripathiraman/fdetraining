from typing import Any, Dict, List, Optional
import repository
from models import PaymentTracker, PaymentTrackerUpdate


# Business logic - add payment record
def add_payment_srv(payment: PaymentTracker) -> Dict[str, Any]:
    return repository.create_payment_record(payment)


# Business logic - get all payment records
def get_all_payments_srv() -> List[Dict[str, Any]]:
    return repository.get_all_records()


# Business logic - get payment record by transaction id
def get_payment_srv(transaction_id: str) -> Optional[Dict[str, Any]]:
    return repository.find_by_transaction_id(transaction_id)


# Business logic - update payment record
def update_payment_srv(transaction_id: str, payment: Any) -> Optional[Dict[str, Any]]:
    if hasattr(payment, "model_dump"):
        data = payment.model_dump(exclude_unset=True)
    elif hasattr(payment, "dict"):
        data = payment.dict(exclude_unset=True)
    elif isinstance(payment, dict):
        data = dict(payment)
    else:
        data = {}
    data["transaction_id"] = transaction_id
    return repository.update_payment_record(data)


# Business logic - delete payment record
def delete_payment_srv(transaction_id: str) -> bool:
    return repository.delete_payment_record(transaction_id)
