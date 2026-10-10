import repository
from models import Invoice

#business logic add invoice
def add_invoices_srv(invoice):
    return repository.add_invoices(invoice)

#business logic get all invoices
def get_all_invoices():
    return repository.load_invoices()

#business logic update invoice
def update_invoices_srv(invoice):
    return repository.update_invoices(invoice)

#business logic delete invoice
def delete_invoices_srv(invoice_id):
    return repository.delete_invoices(invoice_id)

#business logic get invoice by id
def get_invoice_srv(invoice_id):
    return repository.find_invoice(invoice_id)

