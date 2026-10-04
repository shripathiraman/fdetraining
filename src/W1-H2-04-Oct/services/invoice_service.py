import json
from pathlib import Path


INVOICES_FILE = Path(__file__).parent.parent / "data" / "invoices.json"


def _read_invoices():
	with INVOICES_FILE.open(encoding="utf-8") as file:
		return json.load(file)


def _write_invoices(invoices):
	with INVOICES_FILE.open("w", encoding="utf-8") as file:
		json.dump(invoices, file, indent=4)


def get_invoices():
	return _read_invoices()


def get_invoice(invoice_id: int):
	return next(
		(invoice for invoice in _read_invoices() if invoice["invoice_id"] == invoice_id),
		None,
	)


def create_invoice(vendor: str, amount: float, status: str):
	invoices = _read_invoices()
	new_invoice = {
		"invoice_id": max((invoice["invoice_id"] for invoice in invoices), default=0) + 1,
		"vendor": vendor,
		"amount": amount,
		"status": status,
	}
	invoices.append(new_invoice)
	_write_invoices(invoices)
	return new_invoice


def update_invoice(invoice_id: int, vendor: str, amount: float, status: str):
	invoices = _read_invoices()
	invoice = next(
		(invoice for invoice in invoices if invoice["invoice_id"] == invoice_id),
		None,
	)
	if invoice is None:
		return None

	invoice.update({"vendor": vendor, "amount": amount, "status": status})
	_write_invoices(invoices)
	return invoice


def delete_invoice(invoice_id: int):
	invoices = _read_invoices()
	invoice = next(
		(invoice for invoice in invoices if invoice["invoice_id"] == invoice_id),
		None,
	)
	if invoice is None:
		return False

	invoices.remove(invoice)
	_write_invoices(invoices)
	return True
