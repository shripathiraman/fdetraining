from fastapi import FastAPI, APIRouter 
from get_invoices import router as get_invoices
from create_invoice import router as create_invoice
from get_employee import router as get_employee
from create_employee import router as create_employee

app = FastAPI(title="FDE Week 1 API Invoices")


@app.get("/")
def read_root():
	return {"message": "API is running"}


app.include_router(get_invoices)
app.include_router(create_invoice)
app.include_router(get_employee)
app.include_router(create_employee)
