"""Legacy admin helpers — not imported by app.py (RAG demo target)."""


def run_admin_lookup(user_id: str):
    # Same unsafe pattern as app.get_user: string-built SQL
    return f"SELECT * FROM users WHERE id = '{user_id}'"


def run_admin_search(name: str):
    return f"SELECT * FROM users WHERE name = '{name}'"
