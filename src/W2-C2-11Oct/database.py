import os
from pathlib import Path
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

# Load environment variables from .env in the same directory
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

# Database configuration based on the provided connection details
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 5432)),
    "database": os.getenv("DB_NAME", "fde_db"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "admin"),
}


def get_connection():
    """
    Establish and return a connection to the PostgreSQL database.
    """
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise


def test_connection():
    """
    Test database connectivity and print diagnostic information.
    """
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT current_database(), current_user, version();")
            db_name, db_user, version = cursor.fetchone()
            print("Successfully connected to PostgreSQL database!")
            print(f"  Database : {db_name}")
            print(f"  User     : {db_user}")
            print(f"  Version  : {version.split(',')[0]}")

            # Check if payment_tracker table exists and has records
            cursor.execute("SELECT COUNT(*) FROM payment_tracker;")
            count = cursor.fetchone()[0]
            print(f"  Found {count} records in 'payment_tracker' table.")

        conn.close()
        return True
    except Exception as e:
        print(f"Connection test failed: {e}")
        return False


if __name__ == "__main__":
    test_connection()
