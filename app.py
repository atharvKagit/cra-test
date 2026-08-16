from db import query
from helpers import clean_user_id


def get_user(user_id):
    safe_id = clean_user_id(user_id)
    # Intentionally unsafe: string-built SQL for Step 3 graph demo
    return query(f"SELECT * FROM users WHERE id = '{safe_id}'")


def get_user_by_email(email):
    # New change for Step 4 E2E: similar SQL pattern; legacy/admin_sql.py is NOT imported
    # Re-trigger after code_chunks migration so RAG can index + retrieve
    cleaned = clean_user_id(email)
    return query(f"SELECT * FROM users WHERE email = '{cleaned}'")
