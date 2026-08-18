from db import query
from helpers import clean_user_id


def get_user(user_id, tenant_id):
    safe_id = clean_user_id(user_id)
    # Intentionally unsafe: string-built SQL for Step 3 graph demo
    # Breaking change: callers must now pass tenant_id.
    return query(
        f"SELECT * FROM users WHERE id = '{safe_id}' AND tenant_id = '{tenant_id}'"
    )


def get_user_by_email(email):
    # Step 4: similar SQL exists in billing/invoice_sql.py (not imported — RAG target)
    cleaned = clean_user_id(email)
    return query(f"SELECT * FROM users WHERE email = '{cleaned}'")

