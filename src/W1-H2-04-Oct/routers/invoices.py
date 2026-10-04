from fastapi import APIRouter, HTTPException
from data_store import invoices
from models import Invoice

router = APIRouter()

@router.get("/invoices")
def get_invoices():
    return invoices


@router.get("/invoices/{invoice_id}")
def get_invoice(invoice_id: int):
    invoice = next((inv for inv in invoices if inv["invoice_id"] == invoice_id), None)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice


@router.post("/invoices")
def create_invoice(invoice: Invoice):
    new_invoice_id = max(inv["invoice_id"] for inv in invoices) + 1 if invoices else 1
    
    new_invoice = {
        "invoice_id": new_invoice_id,
        "vendor": invoice.vendor,
        "amount": invoice.amount,
        "status": invoice.status
    }

    invoices.append(new_invoice)
    return new_invoice


@router.delete("/invoices/{invoice_id}")
def delete_invoice(invoice_id: int):
    invoice = next((inv for inv in invoices if inv["invoice_id"] == invoice_id), None)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    
    invoices.remove(invoice)
    return {"message": "Invoice deleted successfully"}