import pytest
from app import app
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


def test_post_user_code(client):
    user = {
        "name": "aaaa",
        "lastname": "bbb"}
    response = client.post("/users", json=user)
    assert response.status_code == 201


def test_patch_user_code(client):
    id = 3
    user = {"name": "blabla"}
    response = client.patch(f"/users/{id}", json=user)
    assert response.status_code == 204


def test_put_user_code(client):
    id = 8
    user = {"name": "Kuba", "lastname": "Niczyporuk"}
    response = client.put(f"/users/{id}", json=user)
    assert response.status_code == 204


def test_delete_user_code(client):
    id = 1
    response = client.delete(f"/users/{id}")
    assert response.status_code == 204
