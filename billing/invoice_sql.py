"""Billing export helpers — not imported by app.py (RAG semantic neighbor)."""


def export_invoices_for_user(user_id: str):
    # Same unsafe pattern as app.get_user_by_email: string-built SQL
    return f"SELECT * FROM invoices WHERE user_id = '{user_id}'"


def export_invoices_by_email(email: str):
    return f"SELECT * FROM invoices WHERE email = '{email}'"
