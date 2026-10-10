from helper import get_invoices

invoices = get_invoices()

seen_ids = set()
duplicates = []

for index, invoice in enumerate(invoices):
    invoice_id = invoice["invoice_id"]

    if invoice_id in seen_ids:
        duplicates.append((index, invoice))
    else:
        seen_ids.add(invoice_id)

print("Duplicates:")
print(duplicates)

vendor_totals = {}
for invoice in invoices:
    vendor = invoice["vendor"]
    amount = invoice["amount"]
    vendor_totals[vendor] = vendor_totals.get(vendor, 0) + amount

print("Totals by vendor:")
print(vendor_totals)

# Report duplicate positions using index for each duplicated invoice_id
positions = {}
for index, invoice in enumerate(invoices):
    invoice_id = invoice["invoice_id"]
    positions.setdefault(invoice_id, []).append(index)

print({invoice_id: indexes for invoice_id, indexes in positions.items() if len(indexes) > 1})


positions = {}
for i, invoice in enumerate(invoices):
    positions.setdefault(invoice["invoice_id"], []).append(i)

print({k: v for k, v in positions.items() if len(v) > 1})