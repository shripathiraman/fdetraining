from fastapi import FastAPI, HTTPException
from models import Invoice
import services

app = FastAPI()

#add invoice
@app.post("/invoices")
def add_invoices(invoice: Invoice):
    return services.add_invoices_srv(invoice)

#get all invoices
@app.get("/invoices")
def get_invoices():
    return services.get_all_invoices()

#get invoice by id
@app.get("/invoices/{id}")
def get_invoice(invoice_id: int):
    result = services.get_invoice_srv(invoice_id) 
    if not result:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return result

#update invoice
@app.put("/invoices/{id}")
def update_invoices(invoice_id: int, invoice: Invoice):
    result = services.update_invoices_srv(invoice)
    if not result:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return result


#delete invoice
@app.delete("/invoices/{id}")
def delete_invoices(invoice_id: int):
    result = services.delete_invoices_srv(invoice_id)
    if not result:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return {"message": "Invoice deleted successfully"}

