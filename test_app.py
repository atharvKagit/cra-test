from app import get_user


def test_get_user_returns_query_result():
    result = get_user("42")
    assert result is not None
