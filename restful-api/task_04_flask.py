from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {}

# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Status endpoint
@app.route('/status')
def status():
    return "OK"

# Return list of usernames
@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))

# Return full user data for a given username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Add a new user via POST
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    # Check if "username" is provided
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Store the user
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

# Only run the server when this file is executed directly
if __name__ == "__main__":
    app.run()
