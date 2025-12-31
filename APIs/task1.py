from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id":1, "name":"Bushra"},
    {"id":2, "name":"Fatima"}
]

@app.route('/')
def home():
    return jsonify({
        "message" : "API is working"
    })

@app.route('/users')
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>')
def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user),200

    return jsonify({
     "error": "user not found"
    }),404


if __name__ == '__main__':
    app.run(debug=True)