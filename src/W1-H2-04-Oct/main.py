from fastapi import FastAPI
from routers.invoices import router as invoices_router

app = FastAPI(title="FDE Week 1 - Day 2 - Invoices API", version="1.0.0")
app.include_router(invoices_router)
