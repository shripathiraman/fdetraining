import csv
from collections import defaultdict

INPUT_FILE = "./data/homework_invoices.csv"
OUTPUT_VALID = "./src/W1-H1-03Oct/output/amount_gt_100k.csv"
OUTPUT_ERROR = "./src/W1-H1-03Oct/output/amount_err.csv"

ALLOWED_STATUSES = {"PENDING","REVIEW","APPROVED"}

# ---------------------------------------------------------
# 1. Read CSV
# ---------------------------------------------------------
def read_invoices(filepath):
    with open(filepath, mode='r') as file:
        return list(csv.DictReader(file))


# ---------------------------------------------------------
# 2. Validate a single invoice (business rules)
# ---------------------------------------------------------
def validate_invoice(row):
    errors = []

    # Rule: Vendor must not be empty
    vendor = row.get("vendor", "").strip()
    if not vendor:
        errors.append("Missing vendor")

    # Rule: Status must be valid
    status = row.get("status", "").strip()
    if not status or status not in ALLOWED_STATUSES:
        errors.append(f"Invalid status: {status}")

    # Rule: Amount must be valid float
    try:
        amount = float(row["amount"])
        if amount <= 0:
            errors.append(f"Non‑positive amount: {amount}")
    except Exception:
        errors.append(f"Invalid amount format: {row['amount']}")
        amount = None

    return errors, amount


# ---------------------------------------------------------
# 3. Process invoices
# ---------------------------------------------------------
def process_invoices(invoices):
    valid_invoices = []
    error_invoices = []
    vendor_totals = defaultdict(float)

    processed = 0
    invalid = 0
    high_value = 0

    for row in invoices:
        errors, amount = validate_invoice(row)

        if errors:
            row["errors"] = "; ".join(errors)
            error_invoices.append(row)
            invalid += 1
            continue

        processed += 1

        # Business Rule: High-value invoices
        if amount > 100000:
            valid_invoices.append(row)
            high_value += 1
            vendor_totals[row["vendor"]] += amount

    return valid_invoices, error_invoices, vendor_totals, processed, invalid, high_value


# ---------------------------------------------------------
# 4. Write CSV helper
# ---------------------------------------------------------
def write_csv(filepath, rows):
    if not rows:
        return

    with open(filepath, mode='w', newline='', encoding="utf-8") as file:
        fieldnames = rows[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


# ---------------------------------------------------------
# 5. Dashboard summary
# ---------------------------------------------------------
def print_summary(total, processed, invalid, high_value, vendor_totals):
    print("\n" + "="*60)
    print("                 INVOICE PROCESSING SUMMARY")
    print("="*60)

    print(f"{'Total Input Invoices':25} : {total}")
    print(f"{'Processed Successfully':25} : {processed}")
    print(f"{'Invalid / Error Rows':25} : {invalid}")
    print(f"{'High-value (> ₹100k)':25} : {high_value}")

    print("="*60)
    print("                 VENDOR TOTALS (₹)")
    print("="*60)

    for vendor, total in vendor_totals.items():
        print(f"{vendor:25} : {total:,.2f}")


# ---------------------------------------------------------
# 6. Main Orchestration
# ---------------------------------------------------------
def main():
    invoices = read_invoices(INPUT_FILE)
    total = len(invoices)

    valid, errors, vendor_totals, processed, invalid, high_value = process_invoices(invoices)

    write_csv(OUTPUT_VALID, valid)
    write_csv(OUTPUT_ERROR, errors)

    print_summary(total, processed, invalid, high_value, vendor_totals)


# Run the program
if __name__ == "__main__":
    main()
