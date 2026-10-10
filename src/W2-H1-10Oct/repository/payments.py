import json

DATA_PAYMENTS_FILE = "data/payments.json"


def read_all_payments() -> list:
    with open(DATA_PAYMENTS_FILE, 'r') as file:
        return json.load(file)


def write_all_payments(payments: list) -> None:
    with open(DATA_PAYMENTS_FILE, 'w') as file:
        json.dump(payments, file, indent=4)


def add_payment(payment: dict) -> None:
    payments = read_all_payments()
    payments.append(payment)
    write_all_payments(payments)


def get_payment_by_id(invoice_id: str) -> dict:
    payments = read_all_payments()
    for payment in payments:
        if payment['invoice_id'] == invoice_id:
            return payment
    return None


def update_payment(invoice_id: str, payment: dict) -> None:
    payments = read_all_payments()
    for payment in payments:
        if payment['invoice_id'] == invoice_id:
            payment.update(payment)
            write_all_payments(payments)
            return
    raise ValueError(f"Payment with ID {invoice_id} not found")


def delete_payment(invoice_id: str) -> None:
    payments = read_all_payments()
    payments = [payment for payment in payments if payment['invoice_id'] != invoice_id]
    write_all_payments(payments)


