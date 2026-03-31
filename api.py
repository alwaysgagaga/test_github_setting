from flask import Flask, jsonify

app = Flask(__name__)

USERS = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "role": "admin"},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "role": "user"},
]


@app.route("/api/users")
def get_users():
    """Return user list with email included in response."""
    return jsonify(USERS)


@app.route("/api/users/<int:user_id>")
def get_user(user_id):
    """Return single user by ID."""
    for user in USERS:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"error": "not found"}), 404
