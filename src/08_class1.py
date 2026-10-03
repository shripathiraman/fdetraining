invoices= [{
    "amount": 25000,
    "name": "Invoice 1",
    "customer": "Shripathi Raman Radhakrishnan"
    },{
        "amount": 35000,
        "name": "Invoice 2",
        "customer": "Arthi Shripathi Raman"
    },{
        "amount": 300,
        "name": "Invoice 3",
        "customer": "Aparajitha Shripathi Raman"
    },{
        "amount": 400,
        "name": "Invoice 4",
        "customer": "Varun Shripathi Raman"
    }
]


for invoice in invoices:
    if invoice["amount"] <1000:
        print(f"{invoice['name']} requires supervisor approval")
    elif invoice["amount"] >= 1000 and invoice["amount"] < 25000:
        print(f"{invoice['name']} requires manager approval")
    elif invoice["amount"] >= 25000 and invoice["amount"] < 100000:
        print(f"{invoice['name']} requires manager & director approval")

# dont use the match case when we have conditions checks
for invoice in invoices:
    amount = invoice["amount"]

    match amount:
        case a if a < 1000:
            print(f"{invoice['name']} requires supervisor approval")

        case a if 1000 <= a < 25000:
            print(f"{invoice['name']} requires manager approval")

        case a if 25000 <= a < 100000:
            print(f"{invoice['name']} requires manager & director approval")

        case _:
            print(f"{invoice['name']} requires executive approval")

