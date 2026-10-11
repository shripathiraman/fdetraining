import repository.payments as repo
from models.payments import Payments

# Read the payments from the JSON file
def read_all_payments():
    return repo.read_all_payments()

read_payments = read_all_payments

# Write the payments to the JSON file
def write_payments(payments):
    return repo.write_all_payments(payments)

# create payment in the JSON file
def create_payment(payment: Payments | dict):
    payment_dict = payment.dict() if isinstance(payment, Payments) else dict(payment)
    repo.add_payment(payment_dict)
    return payment

# Read the payment by id from the JSON file
def read_payment_by_id(payment_id: str):
    return repo.get_payment_by_id(payment_id)

# Update the payment in the JSON file
def update_payment(invoice_id: str, payment: Payments | dict) -> Payments | None:
    existing = repo.get_payment_by_id(invoice_id)
    if not existing:
        return None
    if isinstance(payment, Payments):
        payment_dict = payment.dict()
    else:
        payment_dict = dict(payment)
    payment_dict['invoice_id'] = invoice_id
    repo.update_payment(invoice_id, payment_dict)
    return Payments(**payment_dict)

# Delete the payment from the JSON file
def delete_payment(payment_id: str) -> bool:
    existing = repo.get_payment_by_id(payment_id)
    if not existing:
        return False
    repo.delete_payment(payment_id)
    return True

# remove the duplicates entries where the invoice_id and paid are the same
def remove_duplicate_payments(payments):
    return [dict(t) for t in {tuple(d.items()) for d in payments}]  

