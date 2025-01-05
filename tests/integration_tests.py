import pytest
from app import app
from app import post_user
from app import patch_user
from app import put_user
from app import delete_user


@pytest.fixture
def client():
    return app.test_client()

def test_get_all_users_code(client):
    responce = client.get("/users")
    assert responce.status_code == 200


def test_get_one_user_code(client):
    responce = client.get("/users/2")
    assert responce.status_code == 200


def test_post_user_code():
    user = {
        "name": "aaaa",
        "lastname": "bbb"}

    assert post_user(user) == 201


def test_patch_user_code():
    id = 2
    user = {"name":"blabla"}
    assert patch_user(id, user) == 204


def test_put_user_code():
    id = 8
    user = {"name": "Kuba", "lastname": "Niczyporuk"}
    assert put_user(id, user) == 204


def test_delete_user_code():
    id = 1
    assert delete_user(id) == 204
