from flask import Flask, request, jsonify
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.config['secret_key'] = 'my_super_secret_key'

users = []
@app.route('/register', methods=['POST'])
def register():
    data = request.json

    for user in users:
        if user['email'] == data['email']:
            return jsonify({
                "message": "Account already exists",
                "status": 0,
                "data": {},
                "code": 400
            })
    hashed_password = generate_password_hash(data['password'])

    new_user = {
        "id": len(users) + 1,
        "full_name": data['full_name'],
        "email": data['email'],
        "password":hashed_password,
        "country_code": data['country_code'],
        "phone_number": data['phone_number'],
        "user_type":"AppUser"
    }

    users.append(new_user)

    return jsonify({
        "message": "You have registered successfully.",
        "status": 1,
        "data": {
            "country_code": new_user['country_code'],
            "email": new_user['email'],
            "full_name": new_user['full_name'],
            "phone_number": new_user['phone_number']
        },
        "code": 201
    })

@app.route('/login', methods=['POST'])
def login():
    data = request.json

    user = next((u for u in users if u['email'] == data['email']), None)

    if not user:
        return jsonify({
            "message": "Account does not exist",
            "status": 0,
            "data": {},
            "code": 404
        })
    
    if not check_password_hash(user['password'], data['password']):
        return jsonify({
            "message": "Invalid password",
            "status": 0, 
            "data": {},
            "code": 401
        })

    token = jwt.encode({
        "public_id": user['id'],
        "user_type": user['user_type'],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }, app.config['secret_key'], algorithm="HS256")

    return jsonify({
        "message": "You have logged in Successfully.",
        "status": 1,
        "token": token,
        "data": {
            "country_code": user['country_code'],
            "email": user['email'],
            "full_name": user['full_name'],
            "phone_number": user['phone_number']
        },
        "code": 200
    })

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "AUthorization" in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({
                "message": "Token missing",
                "status": 0,
                "code": 401
            })

        try:
            jwt.decode(token, app.config['secret_key'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({
                "message": "Token expired",
                "status": 0,
                "code": 401
            })
        except jwt.InvalidTokenError:
            return jsonify({
                "message": "Invalid token",
                "status": 0,
                "code": 401
            })
        return f(*args, **kwargs)

    return decorated

@app.route('/profile', methods=['GET'])
@token_required
def profile():
    return jsonify({
        "message": "Token is valid, access granted",
        "status": 1,
        "code": 200
    })

if __name__ == '__main__':
    app.run(debug=True)





