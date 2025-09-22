__author__ = 'Mihail Mihaylov'

import pytest

from src.algorithms.patterns.access_control import (
    get_admin_password,
    get_user_password,
)


def test_admin_allows_admin_user() -> None:
    assert get_admin_password({"secure_level": "admin", "password": 10000}) == 10000


def test_admin_denies_guest_user() -> None:
    with pytest.raises(PermissionError):
        get_admin_password({"secure_level": "guest", "password": 123456})


def test_guest_allows_guest_user() -> None:
    assert get_user_password({"secure_level": "guest", "password": 123456}) == 123456


def test_missing_user_mapping_raises() -> None:
    with pytest.raises(ValueError):
        get_admin_password()
