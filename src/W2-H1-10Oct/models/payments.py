from pydantic import BaseModel

class Payments(BaseModel):
    invoice_id: str
    paid: float