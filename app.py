from flask import Flask
from flask import Flask, request, jsonify

users = {
    0: {"name": "John", "lastname": "Doe"},
    1: {"name": "Jane", "lastname": "Smith"},
    2: {"name": "Robert", "lastname": "Brown"},
    3: {"name": "Emily", "lastname": "Davis"},
    4: {"name": "Michael", "lastname": "Wilson"}
}


app = Flask(__name__)


def find_first_free_id():
    for id in users:
        if users[id] is None:
            return id
    return len(users)


@app.get('/users')
def get_users():
    return users


@app.get('/users/<int:id>')
def get_user(id):
    return users[id]

@app.post('/users')
def post_user(user):
    id = find_first_free_id()
    users[id] = {"name": user["name"], "lastname": user["lastname"]}
    return 201


@app.patch('/users/<int:id>')
def patch_user(id, user):
    if id <= len(users) or users[id] is not None:
        if len(user) == 1:
            key = list(user.keys())
            if key[0] == 'name':
                users[id] = {"name": user["name"], "lastname": users[id]["lastname"]}
                return 204
            elif key[0] == "lastname":
                users[id] = {"name": users[id]["name"], "lastname": user["lastname"]}
                return 204
    return 400


@app.put("/users/<int:id>")
def put_user(id, user):
    if id > len(users):
        id = len(users)
    users[id] = {"name": user["name"], "lastname": user["lastname"]}
    return 204


@app.delete("/users/<int:id>")
def delete_user(id):
    if id <= len(users) and users[id] is not None:
        users[id] = None
        return 204
    return 400


if __name__ == '__main__':
    app.run()
