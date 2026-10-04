from pydantic import BaseModel

class Invoice(BaseModel):
    id: int
    amount: float
    status: str

class Employee(BaseModel):
    id: int
    name: str
    department: str