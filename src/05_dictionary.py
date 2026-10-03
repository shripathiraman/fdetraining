invoice ={
    "invoice_number": "INV-001",
    "date": "2023-06-01",
    "customer": {
        "name": "John Doe",
        "address": "123 Main St, Anytown, USA"
    },
    "items": [
        {"description": "Widget A", "quantity": 2, "unit_price": 10.0},
        {"description": "Widget B", "quantity": 1, "unit_price": 20.0}
    ],
}

print(invoice["invoice_number"])  # Output: INV-001
print(invoice["date"])  # Output: 2023-06-01
print(invoice["customer"]["name"])  # Output: John Doe
print(invoice["customer"]["address"])  # Output: 123 Main St, Anytown, USA
print(invoice["items"][0]["description"])  # Output: Widget A
print(invoice["items"][0]["quantity"])  # Output: 2
print(invoice["items"][0]["unit_price"])  # Output: 10.0