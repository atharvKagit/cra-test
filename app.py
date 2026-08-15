from db import query
from helpers import clean_user_id


def get_user(user_id):
    safe_id = clean_user_id(user_id)
    # Intentionally unsafe: string-built SQL for Step 3 graph demo
    return query(f"SELECT * FROM users WHERE id = '{safe_id}'")
