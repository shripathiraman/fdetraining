# pyrefly: ignore [missing-import]
import repository.invoices as repo
from models.invoices import Invoices


# Read all invoices from the JSON file
def read_all_invoices() -> list[Invoices]:
    invoices_data = repo.read_all_invoices()
    return [Invoices(**inv) for inv in invoices_data]


# Write all invoices to the JSON file
def write_all_invoices(invoices: list[Invoices]) -> list[Invoices]:
    invoices_data = [inv.dict() for inv in invoices]
    repo.write_all_invoices(invoices_data)
    return invoices


# Add the invoice to the JSON file
def create_invoice(invoice: Invoices) -> Invoices:
    repo.add_invoice(invoice.dict())
    return invoice


# Get the invoice by id from the JSON file
def read_invoice_by_id(invoice_id: str) -> Invoices | None:
    invoice_data = repo.get_invoice_by_id(invoice_id)
    if invoice_data:
        return Invoices(**invoice_data)
    return None


# Update the invoice in the JSON file
def update_invoice(invoice_id: str, invoice: Invoices) -> Invoices | None:
    existing = repo.get_invoice_by_id(invoice_id)
    if not existing:
        return None
    updated_data = invoice.dict()
    updated_data['invoice_id'] = invoice_id
    repo.update_invoice(invoice_id, updated_data)
    return Invoices(**updated_data)


# Delete the invoice from the JSON file
def delete_invoice(invoice_id: str) -> bool:
    existing = repo.get_invoice_by_id(invoice_id)
    if not existing:
        return False
    repo.delete_invoice(invoice_id)
    return True


# Normalize the invoices by removing extra spaces and changing the status to upper case
def normalize_invoices(invoices: list[dict]) -> list[dict]:
    for invoice in invoices:
        if 'vendor' in invoice and invoice['vendor']:
            invoice['vendor'] = invoice['vendor'].strip().title()
        if 'status' in invoice and invoice['status']:
            invoice['status'] = invoice['status'].upper()
    return invoices


# Exact duplicates. Build an exact_dupes dict that maps each duplicated key to a list of its indexes. 
# Keep the first row of each group and remove the rest.
def find_exact_duplicates(invoices: list[dict]) -> dict:
    exact_dupes = {}
    for index, invoice in enumerate(invoices):
        # Sort items to ensure stable hashing
        items = tuple(sorted((k, v) for k, v in invoice.items() if isinstance(v, (str, int, float, bool, type(None)))))
        if items in exact_dupes:
            exact_dupes[items].append(index)
        else:
            exact_dupes[items] = [index]
    return exact_dupes


# remove the duplicates from the list of invoices
def remove_duplicates(invoices: list[dict], exact_dupes: dict) -> list[dict]:
    indices_to_remove = set()
    for indices in exact_dupes.values():
        indices_to_remove.update(indices[1:])
    return [inv for idx, inv in enumerate(invoices) if idx not in indices_to_remove]


# Report any row where amount is None, with its index, and exclude it from the later totals.
def find_amount_null(invoices: list[dict]) -> list:
    null_amount_invoices = []
    for index, invoice in enumerate(invoices):
        if invoice.get('amount') is None:
            null_amount_invoices.append((index, invoice))
    return null_amount_invoices


# remove the null amount invoices from the list of invoices
def remove_null_amount_invoices(invoices: list[dict]) -> list[dict]:
    return [invoice for invoice in invoices if invoice.get('amount') is not None]


# Suspected duplicates. Find rows that match on vendor, amount and date but have different IDs. 
# Print them as pairs, (INV-107 ~ INV-101), and don't remove them.
def find_suspected_duplicates(invoices: list[dict]) -> list:
    suspected_dupes = []
    for index, invoice in enumerate(invoices):
        for index2, invoice2 in enumerate(invoices):
            if (index < index2 and 
                invoice.get('vendor') == invoice2.get('vendor') and 
                invoice.get('amount') == invoice2.get('amount') and 
                invoice.get('date') == invoice2.get('date')):
                suspected_dupes.append((index, index2))
    return suspected_dupes


# Credit notes. Match each negative invoice to its positive partner. 
# Mark both as "CANCELLED" and exclude them from totals. Print the index pair. 
# Handle a credit note with no partner.
def process_credit_notes(invoices: list[dict]) -> list[dict]:
    for credit_index, credit_invoice in enumerate(invoices):
        amount = credit_invoice.get("amount")
        if amount is not None and amount < 0:
            partner_found = False
            for positive_index, positive_invoice in enumerate(invoices):
                pos_amount = positive_invoice.get("amount")
                if (
                    positive_invoice.get("vendor") == credit_invoice.get("vendor")
                    and pos_amount is not None and pos_amount > 0
                    and pos_amount == abs(amount)
                    and positive_invoice.get("status") != "CANCELLED"
                ):
                    credit_invoice["status"] = "CANCELLED"
                    positive_invoice["status"] = "CANCELLED"
                    print(f"{credit_index} <-> {positive_index}")
                    partner_found = True
                    break
            if not partner_found:
                print(f"No partner found for invoice {credit_invoice.get('invoice_id')}")
    return invoices


# Remove cancelled invoices from the list of invoices
def remove_cancelled_invoices(invoices: list[dict]) -> list[dict]:
    return [invoice for invoice in invoices if invoice.get('status') != 'CANCELLED']

