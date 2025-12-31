from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
   {"id":1, "name": "Alifa", "email": "alifamemon@gmail.com"},
   {"id":2, "name":"Muskan", "email": "muskanmemon@gmail.com"}
]

@app.route('/')
def home():
    return jsonify({"message":"POST Users API is working"})

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users),200

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json

    if not data:
        return jsonify({"error": "JSON body required"}),400

    if "name" not in data or data["name"].strip() == "":
        return jsonify({"error": "Name cannot be empty"}),400

    if "email" not in data or data["email"].strip() == "":
        return jsonify({"error": "Email is required"}), 400

    new_user = {
        "id" : len(users) + 1,
        "name" : data["name"],
        "email" : data["email"]
    }

    users.append(new_user)

    return jsonify({
        "message": "user added successfully",
        "user": new_user
    }),201

if __name__ == '__main__':
    app.run(debug=True)





