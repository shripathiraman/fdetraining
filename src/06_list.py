invoices = ["Invoice 1", "Invoice 2", "Invoice 3"]

invoices1 = [
    {
        "invoice_number": "INV-001",
        "date": "2023-06-01",
        "customer": {
            "name": "John Doe",
            "address": "123 Main St, Anytown, USA"
        },
        "items": [
            {"description": "Widget A", "quantity": 2, "unit_price": 10.0},
            {"description": "Widget B", "quantity": 1, "unit_price": 20.0}
        ]
    },
    {
        "invoice_number": "INV-002",
        "date": "2023-06-02",
        "customer": {
            "name": "Jane Smith",
            "address": "456 Elm St, Othertown, USA"
        },
        "items": [
            {"description": "Widget C", "quantity": 3, "unit_price": 15.0},
            {"description": "Widget D", "quantity": 2, "unit_price": 25.0}
        ]
    },
    {
        "invoice_number": "INV-003",
        "date": "2023-06-03",
        "customer": {
            "name": "Bob Johnson",
            "address": "789 Oak St, Yet another town, USA"
        },
        "items": [
            {"description": "Widget E", "quantity": 1, "unit_price": 30.0},
            {"description": "Widget F", "quantity": 2, "unit_price": 35.0}
        ]
    }
]

print(invoices1[0]["invoice_number"])  # Output: INV-001

invoices1[0]["customer"]["name"] = "Shripathi Raman Radhakrishnan"

invoices1.append({
    "invoice_number": "INV-004",
    "date": "2023-06-04",
    "customer": {
        "name": "Alice Brown",
        "address": "101 Pine St, Newtown, USA"
    },
    "items": [
        {"description": "Widget G", "quantity": 1, "unit_price": 40.0},
        {"description": "Widget H", "quantity": 2, "unit_price": 45.0}
    ]
})


for invoice in invoices:
    print(invoice)  # Output: Invoice 1, Invoice 2, Invoice 3

for invoice in invoices1:
    print(invoice["invoice_number"])  # Output: INV-001, INV-002, INV-003
    print(invoice["date"])  # Output: 2023-06-01, 2023-06-02, 2023-06-03
    print(invoice["customer"]["name"])  # Output: John Doe, Jane Smith, Bob Johnson
    print(invoice["customer"]["address"])  # Output: 123 Main St, Anytown, USA, 456 Elm St, Othertown, USA, 789 Oak St, Yet another town, USA
    for item in invoice["items"]:
        print(item["description"])  # Output: Widget A, Widget B, Widget C, Widget D, Widget E, Widget F
        print(item["quantity"])  # Output: 2, 1, 3, 2, 1, 2
        print(item["unit_price"])  # Output: 10.0, 20.0, 15.0, 25.0, 30.0, 35.0