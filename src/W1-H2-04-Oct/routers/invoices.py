from fastapi import APIRouter, HTTPException
from models import Invoice
from services import invoice_service

router = APIRouter()

@router.get("/invoices")
def get_invoices():
    return invoice_service.get_invoices()


@router.get("/invoices/{invoice_id}")
def get_invoice(invoice_id: int):
    invoice = invoice_service.get_invoice(invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice


@router.post("/invoices")
def create_invoice(invoice: Invoice):
    return invoice_service.create_invoice(invoice.vendor, invoice.amount, invoice.status)


@router.delete("/invoices/{invoice_id}")
def delete_invoice(invoice_id: int):
    if not invoice_service.delete_invoice(invoice_id):
        raise HTTPException(status_code=404, detail="Invoice not found")
    return {"message": "Invoice deleted successfully"}


@router.put("/invoices/{invoice_id}")
def update_invoice(invoice_id: int, invoice: Invoice):
    updated_invoice = invoice_service.update_invoice(invoice_id, invoice.vendor, invoice.amount, invoice.status)
    if not updated_invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return updated_invoice
