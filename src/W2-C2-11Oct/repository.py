from decimal import Decimal
from typing import Any, Dict, List, Optional
from psycopg2.extras import RealDictCursor

from database import get_connection
from models import PaymentTracker


def _format_row(row: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """Convert RealDictRow to standard Python dictionary with numeric amounts as floats."""
    if not row:
        return None
    data = dict(row)
    if isinstance(data.get("amount"), Decimal):
        data["amount"] = float(data["amount"])
    return data


# CRUD Repository Methods - Fetch all records
def get_all_records() -> List[Dict[str, Any]]:
    """Fetch all payment tracker records from the database."""
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM payment_tracker ORDER BY transaction_date DESC;")
            rows = cur.fetchall()
            return [_format_row(row) for row in rows]
    finally:
        conn.close()


# CRUD Repository Methods - Fetch record by transaction id
def find_by_transaction_id(transaction_id: str) -> Optional[Dict[str, Any]]:
    """Fetch a single payment tracker record by its transaction_id."""
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "SELECT * FROM payment_tracker WHERE transaction_id = %s;",
                (str(transaction_id),),
            )
            row = cur.fetchone()
            return _format_row(row)
    finally:
        conn.close()


# CRUD Repository Methods - Create tracker record
def create_payment_record(record: Any) -> Dict[str, Any]:
    """
    Insert a new payment tracker record into the database.
    Accepts a PaymentTracker Pydantic model or a dictionary.
    """
    if hasattr(record, "model_dump"):
        data = record.model_dump()
    elif hasattr(record, "dict"):
        data = record.dict()
    elif isinstance(record, dict):
        data = dict(record)
    else:
        raise ValueError("Invalid record format. Expected PaymentTracker model or dict.")

    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                INSERT INTO payment_tracker (
                    transaction_id,
                    transaction_date,
                    sender_name,
                    receiver_name,
                    amount,
                    payment_mode,
                    status,
                    remarks
                ) VALUES (
                    %(transaction_id)s,
                    %(transaction_date)s,
                    %(sender_name)s,
                    %(receiver_name)s,
                    %(amount)s,
                    COALESCE(%(payment_mode)s, 'GPay'),
                    COALESCE(%(status)s, 'SUCCESS'),
                    %(remarks)s
                )
                RETURNING *;
                """,
                {
                    "transaction_id": data.get("transaction_id"),
                    "transaction_date": data.get("transaction_date"),
                    "sender_name": data.get("sender_name"),
                    "receiver_name": data.get("receiver_name"),
                    "amount": data.get("amount"),
                    "payment_mode": data.get("payment_mode", "GPay"),
                    "status": data.get("status", "SUCCESS"),
                    "remarks": data.get("remarks"),
                },
            )
            created_row = cur.fetchone()
            conn.commit()
            return _format_row(created_row)
    except Exception as e:
        conn.rollback()
        print(f"Error creating payment tracker record: {e}")
        raise
    finally:
        conn.close()


# CRUD Repository Methods - Update tracker record
def update_payment_record(record: Any) -> Optional[Dict[str, Any]]:
    """Update an existing payment tracker record by its transaction_id."""
    if hasattr(record, "model_dump"):
        data = record.model_dump(exclude_unset=True)
    elif hasattr(record, "dict"):
        data = record.dict(exclude_unset=True)
    elif isinstance(record, dict):
        data = dict(record)
    else:
        raise ValueError("Invalid record format. Expected PaymentTracker model or dict.")

    transaction_id = data.pop("transaction_id", None)
    if not transaction_id:
        raise ValueError("transaction_id is required for update.")

    # Filter out None values and keys that shouldn't be updated
    data = {k: v for k, v in data.items() if v is not None and k != "created_at"}
    if not data:
        return find_by_transaction_id(transaction_id)

    set_clauses = [f"{col} = %({col})s" for col in data.keys()]
    query = f"""
        UPDATE payment_tracker
        SET {', '.join(set_clauses)}
        WHERE transaction_id = %(transaction_id)s
        RETURNING *;
    """
    data["transaction_id"] = transaction_id

    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, data)
            updated_row = cur.fetchone()
            conn.commit()
            return _format_row(updated_row)
    except Exception as e:
        conn.rollback()
        print(f"Error updating payment tracker record: {e}")
        raise
    finally:
        conn.close()


# CRUD Repository Methods - Delete tracker record
def delete_payment_record(transaction_id: str) -> bool:
    """Delete a payment tracker record by its transaction_id."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM payment_tracker WHERE transaction_id = %s;",
                (str(transaction_id),),
            )
            deleted = cur.rowcount > 0
            conn.commit()
            return deleted
    except Exception as e:
        conn.rollback()
        print(f"Error deleting payment tracker record: {e}")
        raise
    finally:
        conn.close()


# Backward compatibility aliases
load_invoices = get_all_records
find_invoice = find_by_transaction_id
add_invoices = create_payment_record
update_invoices = update_payment_record
delete_invoices = delete_payment_record


if __name__ == "__main__":
    from datetime import datetime

    print("--- 1. Testing get_all_records() ---")
    records = get_all_records()
    print(f"Fetched {len(records)} total records from database.")
    if records:
        print("First record:", records[0])

    print("\n--- 2. Testing find_by_transaction_id('TXN001') ---")
    record = find_by_transaction_id("TXN001")
    print("Found record:", record)

    print("\n--- 3. Testing create_payment_record() ---")
    test_id = f"TXN_TEST_{int(datetime.now().timestamp())}"
    new_tracker = PaymentTracker(
        transaction_id=test_id,
        transaction_date=datetime.now(),
        sender_name="Unit Tester",
        receiver_name="Classroom DB",
        amount=99.99,
        payment_mode="GPay",
        status="SUCCESS",
        remarks="Test creation record",
    )
    created = create_payment_record(new_tracker)
    print("Created record:", created)

    # Clean up test record
    delete_payment_record(test_id)
    print(f"Cleaned up test record {test_id}.")
