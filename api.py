from app import get_user


def handle_user(user_id):
    # Unchanged caller: if get_user SQL changes, this path still executes it.
    return get_user(user_id)
