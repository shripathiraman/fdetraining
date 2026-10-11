# Invoice & Payment Reconciliation API

A FastAPI application for managing invoices and payments with an automated data processing and reconciliation pipeline, built using a clean layered architecture (Routers, Services, Repositories, and Models) with JSON file persistence.

---

## Features

- **Invoices API**: Full CRUD operations for managing invoices (`data/invoices.json`).
- **Payments API**: Full CRUD operations for managing payment transactions (`data/payments.json`).
- **Data Cleaning & Reconciliation Pipeline**:
  - **Normalization**: Trims vendor whitespace, applies title-casing, and standardizes status to uppercase.
  - **Exact Duplicates**: Detects and eliminates identical records while preserving the first instance.
  - **Null Amount Handling**: Identifies records with missing amounts and excludes them from processing.
  - **Suspected Duplicates**: Flags records matching on vendor, amount, and date but carrying different IDs.
  - **Credit Note Matching**: Cancels matching positive and negative amount pairs from the same vendor.
  - **Payment Reconciliation**: Joins unique payments to active invoices by `invoice_id`.

---

## Project Structure

```text
W2-H1-10Oct/
├── data/
│   ├── invoices.json          # Persistent JSON store for invoices
│   └── payments.json          # Persistent JSON store for payments
├── models/
│   ├── invoices.py            # Pydantic schema for Invoices
│   └── payments.py            # Pydantic schema for Payments
├── repository/
│   ├── invoices.py            # Data access layer for invoices.json
│   └── payments.py            # Data access layer for payments.json
├── services/
│   ├── invoices.py            # Invoices business logic & data transformations
│   ├── payments.py            # Payments business logic & deduplication
│   └── reconcilation.py       # End-to-end reconciliation orchestration
├── routers/
│   ├── invoices.py            # API routes for /invoices
│   ├── payments.py            # API routes for /payments
│   └── reconcilation.py       # API route for /reconcile
├── homework.txt               # Assignment requirements & business rules
├── main.py                    # FastAPI application entrypoint
└── README.md                  # Project documentation
```

---

## Getting Started

### 1. Prerequisites
Ensure you have Python 3.10+ and the required packages installed:
```powershell
pip install fastapi uvicorn pydantic
```

### 2. Run the Application
Navigate to the project directory and start the Uvicorn development server:
```powershell
uvicorn main:app --reload
```

- **API Base URL**: `http://127.0.0.1:8000`
- **Interactive Swagger Docs**: `http://127.0.0.1:8000/docs`
- **ReDoc Docs**: `http://127.0.0.1:8000/redoc`

---

## API Endpoints

### Invoices (`/invoices`)

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/invoices` | Retrieve all invoices |
| `GET` | `/invoices/{invoice_id}` | Retrieve a specific invoice by ID |
| `POST` | `/invoices` | Create a new invoice |
| `PUT` | `/invoices/{invoice_id}` | Update an existing invoice by ID |
| `DELETE` | `/invoices/{invoice_id}` | Delete an invoice by ID |

#### Invoice Schema Example:
```json
{
  "invoice_id": "INV-101",
  "vendor": "ABC Ltd",
  "amount": 85000.0,
  "status": "PENDING",
  "date": "2026-09-03"
}
```

---

### Payments (`/payments`)

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/payments` | Retrieve all payments |
| `GET` | `/payments/{payment_id}` | Retrieve a specific payment by ID |
| `POST` | `/payments` | Create a new payment record |
| `PUT` | `/payments/{payment_id}` | Update an existing payment record |
| `DELETE` | `/payments/{payment_id}` | Delete a payment record by ID |

#### Payment Schema Example:
```json
{
  "invoice_id": "INV-101",
  "paid": 85000.0
}
```

---

### Reconciliation (`/reconcile`)

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/reconcile` | Runs the full cleaning and reconciliation pipeline |

#### Sample Reconciliation Response:
```json
{
  "message": "Reconciliation successful",
  "reconciled_payments": [
    {
      "invoice_id": "INV-101",
      "vendor": "ABC Ltd",
      "amount": 85000.0,
      "status": "PENDING",
      "date": "2026-09-03",
      "paid": 85000.0
    },
    {
      "invoice_id": "INV-104",
      "vendor": "ABC Ltd",
      "amount": 62000.0,
      "status": "PAID",
      "date": "2026-09-08",
      "paid": 60000.0
    }
  ]
}
```

---

## Business & Processing Rules

1. **Vendor Normalization**: Vendor names differing only by case or whitespace (e.g. `"xyz corp"` vs `"XYZ Corp"`, `"ABC Ltd "` vs `"ABC Ltd"`) are cleaned into standard Title Case with whitespace trimmed.
2. **Exact Duplicates**: Rows where every field matches are deduplicated, keeping only the first occurrence.
3. **Null Amounts**: Rows with `amount: null` are identified, reported, and excluded from totals.
4. **Suspected Duplicates**: Rows sharing the same vendor, amount, and date but with different IDs (e.g., `INV-107` and `INV-101`) are flagged and reported.
5. **Credit Notes**: Negative amounts cancel matching positive invoices of the exact same absolute value for that vendor. Both are marked as `CANCELLED` and excluded from subsequent totals.
6. **Payment Matching**: Duplicate payment entries are removed, and unique payments are joined with valid active invoices matching on `invoice_id`.
