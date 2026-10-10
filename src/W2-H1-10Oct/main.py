from fastapi import FastAPI
# pyrefly: ignore [missing-import]
from routers.invoices import router as invoices_router
# pyrefly: ignore [missing-import]
from routers.payments import router as payments_router
# pyrefly: ignore [missing-import]
from routers.reconcilation import router as reconcilation_router

# Create the FastAPI app
app = FastAPI(title="FDE Week 2 - Day 1 - Invoice & Payment Reconcilation API", version="1.0.0")
app.include_router(invoices_router)
app.include_router(payments_router)
app.include_router(reconcilation_router)