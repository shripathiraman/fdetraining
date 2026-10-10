from services.invoices import (
    read_all_invoices,
    normalize_invoices,
    find_amount_null,
    find_exact_duplicates,
    remove_null_amount_invoices,
    remove_duplicates,
    process_credit_notes,
    remove_cancelled_invoices,
    find_suspected_duplicates
)
from services.payments import (
    read_payments,
    write_payments,
    remove_duplicate_payments
)


def reconcile_payments(invoices, payments):
    reconciled_payments = []
    for payment in payments:
        for invoice in invoices:
            if payment.get('invoice_id') == invoice.get('invoice_id'):
                # Merge the invoice and payment dictionaries into one
                combined = {**invoice, **payment}
                reconciled_payments.append(combined)
                break
    return reconciled_payments

def run_reconciliation():
    # Read the invoices from the JSON file
    invoices_objs = read_all_invoices()
    invoices = [inv.dict() for inv in invoices_objs] if invoices_objs and hasattr(invoices_objs[0], 'dict') else invoices_objs

    # read the payments from the JSON file
    payments_data = read_payments()
    payments = [pay.dict() for pay in payments_data] if payments_data and hasattr(payments_data[0], 'dict') else payments_data

    print("\nBefore normalization:")
    for invoice in invoices:
        print(invoice)

    # normalize invoices
    invoices = normalize_invoices(invoices)

    # find the invoices with null amount
    invoice_with_null = find_amount_null(invoices)

    # remove the null amount invoices
    invoices = remove_null_amount_invoices(invoices)

    # find the exact duplicates
    exact_dupes = find_exact_duplicates(invoices)

    # remove the duplicates
    invoices = remove_duplicates(invoices, exact_dupes)

    # process the credit notes
    invoices = process_credit_notes(invoices)

    # remove the cancelled invoices
    invoices = remove_cancelled_invoices(invoices)

    # find the suspected duplicates
    suspected_dupes = find_suspected_duplicates(invoices)

    print("\nInvoice with null amount:")
    for index, invoice in invoice_with_null:
        print(index, invoice)

    print("\nExact duplicates:")
    for key, value in exact_dupes.items():
        print(key, value)

    print("\nSuspected duplicates:")
    for index, invoice in suspected_dupes:
        print(index, invoice)

    print("\nAfter normalization, removal of null amounts, duplicates and credit notes:")
    for invoice in invoices:
        print(invoice)

    print("\nPayments:")
    for payment in payments:
        print(payment)

    # remove the duplicates entries where the invoice_id and paid are the same
    payments = remove_duplicate_payments(payments)

    print("\nAfter removal of duplicates:")
    for payment in payments:
        print(payment)
    #write_all_invoices(invoices)

    reconciled_payments = reconcile_payments(invoices, payments)
    print("\nReconciled payments:")
    for combined_record in reconciled_payments:
        print(combined_record)
    
    return reconciled_payments
