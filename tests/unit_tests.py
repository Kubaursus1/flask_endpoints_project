import pytest
from app import app
from app import users
from app import get_users
from app import get_user
from app import patch_user
from app import post_user
from app import put_user
from app import delete_user


def test_get_all_users():
    assert get_users() == users


def test_get_one_user():
    id = 0
    assert get_user(id) == users[id]


def test_post_user():
    user = {
        "name": "aaaa",
        "lastname": "bbb"}
    with app.test_request_context(json=user):
        post_user()

    assert user in users.values()


def test_patch_user():
    id = 2
    key = "name"
    user = {key: "blabla"}
    with app.test_request_context(json=user):
        patch_user(id)
    value = list(user.values())
    assert value[0] == users[id][key]


def test_put_user():
    id = 8
    user = {"name": "Kuba", "lastname": "Niczyporuk"}
    with app.test_request_context(json=user):
        put_user(id)
    assert users[id if id <= len(users) else list(users)[-1]] == user


def test_delete_user():
    id = 1
    user = users[id]
    delete_user(id)
    assert users[id] != user and users[id] is None
