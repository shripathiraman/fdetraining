from anyio import from_thread
import json

DATA_INVOICE_FILE = "data/invoices.json"

# Read all invoices from the JSON file
def read_all_invoices() -> list:
    with open(DATA_INVOICE_FILE, 'r') as file:
        return json.load(file)


# Write all invoices to the JSON file
def write_all_invoices(invoices: list) -> None:
    with open(DATA_INVOICE_FILE, 'w') as file:
        json.dump(invoices, file, indent=4)


# Add the invoice to the JSON file
def add_invoice(invoice: dict) -> None:
    invoices = read_all_invoices()
    invoices.append(invoice)
    write_all_invoices(invoices)


# Get the invoice by id from the JSON file
def get_invoice_by_id(invoice_id: str) -> dict:
    invoices = read_all_invoices()
    for invoice in invoices:
        if invoice['invoice_id'] == invoice_id:
            return invoice
    return None


# Update the invoice in the JSON file
def update_invoice(invoice_id: str, invoice: dict) -> None:
    invoices = read_all_invoices()
    for invoice in invoices:
        if invoice['invoice_id'] == invoice_id:
            invoice.update(invoice)
            write_all_invoices(invoices)
            return
    raise ValueError(f"Invoice with ID {invoice_id} not found")


# Delete the invoice from the JSON file
def delete_invoice(invoice_id: str) -> None:
    invoices = read_all_invoices()
    invoices = [invoice for invoice in invoices if invoice['invoice_id'] != invoice_id]
    write_all_invoices(invoices)

