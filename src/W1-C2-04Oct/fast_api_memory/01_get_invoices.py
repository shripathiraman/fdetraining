from fastapi import FastAPI

app = FastAPI(title="FDE Week 1 API Invoices")

# Sample data representing invoices
invoices = [
    {"id": 1, "amount": 100.0, "status": "paid"},
    {"id": 2, "amount": 200.0, "status": "unpaid"},
    {"id": 3, "amount": 150.0, "status": "paid"},
    {"id": 4, "amount": 300.0, "status": "unpaid"},
    {"id": 5, "amount": 250.0, "status": "paid"}
]

@app.get("/invoices")
def get_invoices():
    return invoices

@app.get("/invoices/{invoice_id}")
def get_invoice(invoice_id: int):
    for invoice in invoices:
        if invoice["id"] == invoice_id:
            return invoice
    return {"error": "Invoice not found"}

