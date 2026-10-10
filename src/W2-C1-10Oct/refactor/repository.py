import json

DATA_FILE = "./data/invoices.json"

def load_invoices():
    with open(DATA_FILE,"r",encoding="utf-8") as f:
        return json.load(f)

def write_invoices(invoices):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(invoices, f, indent=4)

#CRUD repository methods - find invoice
def find_invoice(invoice_id):
    invoices = load_invoices()
    for invoice in invoices:
        if invoice.get("invoice_id") == invoice_id:
            return invoice
    return None

#CRUD repository methods - add invoice
def add_invoices(invoice):
    if hasattr(invoice, "model_dump"):
        invoice = invoice.model_dump()
    elif hasattr(invoice, "dict"):
        invoice = invoice.dict()
    invoices = load_invoices()
    invoices.append(invoice)
    write_invoices(invoices)
    return invoice

#CRUD repository methods - update invoice
def update_invoices(updated_invoice):
    if hasattr(updated_invoice, "model_dump"):
        updated_invoice = updated_invoice.model_dump()
    elif hasattr(updated_invoice, "dict"):
        updated_invoice = updated_invoice.dict()
    invoices = load_invoices()
    for invoice in invoices:
        if invoice.get("invoice_id") == updated_invoice.get("invoice_id"):
            invoice.update(updated_invoice)
            write_invoices(invoices)
            return invoice
    return None

#CRUD repository methods - delete invoice
def delete_invoices(invoice_id):
    invoices = load_invoices()
    for invoice in invoices:
        if invoice.get("invoice_id") == invoice_id:
            invoices.remove(invoice)
            write_invoices(invoices)
            return True
    return False
