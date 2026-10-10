from pydantic import BaseModel

class Invoices(BaseModel):
    invoice_id: str
    vendor: str
    amount: float | None = None
    status: str
    date: str
