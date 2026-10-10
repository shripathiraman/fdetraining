# Invoice API

A small FastAPI application for managing invoices stored in `data/invoices.json`.

## Run the API

Open a terminal in this directory and run:

```powershell
uvicorn main:app --reload
```

The API runs at `http://127.0.0.1:8000`. Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## Endpoints

| Method | URL | Description |
| --- | --- | --- |
| GET | `/invoices` | Get all invoices |
| GET | `/invoices/{invoice_id}` | Get one invoice |
| POST | `/invoices` | Create an invoice |
| PUT | `/invoices/{invoice_id}` | Replace an invoice's vendor, amount, and status |
| DELETE | `/invoices/{invoice_id}` | Delete an invoice |

Invoice request bodies use this JSON shape:

```json
{
  "vendor": "ABC Ltd",
  "amount": 100.0,
  "status": "paid"
}
```

## Update an invoice in Postman

1. Set the method to `PUT`.
2. Enter a URL such as `http://127.0.0.1:8000/invoices/1`.
3. Select **Body**, then **raw** and **JSON**.
4. Send the invoice fields to replace:

```json
{
  "vendor": "ABC Ltd",
  "amount": 125.0,
  "status": "paid"
}
```

The invoice ID belongs in the URL, not the request body. A successful update returns the updated invoice. If the ID does not exist, the API returns `404 Invoice not found`.
