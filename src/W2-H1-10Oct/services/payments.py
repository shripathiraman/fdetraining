import repository.payments as repo
from models.payments import Payments

# create payment in the JSON file
def create_payment(payment):
    return repo.add_payment(payment)

# Read the payments from the JSON file
def read_payments():
    return repo.read_all_payments()

# Write the payments to the JSON file
def write_payments(payments):
    return repo.write_all_payments(payments)

# Read the payment by id from the JSON file
def read_payment_by_id(payment_id):
    return repo.get_payment_by_id(payment_id)

# Update the payment in the JSON file
def update_payment(invoice_id, payment):
    return repo.update_payment(invoice_id, payment)

# Delete the payment from the JSON file
def delete_payment(payment_id):
    return repo.delete_payment(payment_id)

# remove the duplicates entries where the invoice_id and paid are the same
def remove_duplicate_payments(payments):
    return [dict(t) for t in {tuple(d.items()) for d in payments}]  

