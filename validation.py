from marshmallow import Schema, fields, validate,ValidationError
from flask import Flask, request, jsonify 

app = Flask(__name__)

class UserSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))
    age = fields.Int(validate=validate.Range(min=18))


user_schema = UserSchema()

@app.route('/register', methods=['POST'])
def register():
    try:
        data = user_schema.load(request.json)
        return jsonify({
            "message": "Validation successful",
            "data": data
        }),200

    except ValidationError as err:
        return jsonify({
            "errors": err.messages
        }),400

if __name__ == '__main__':
    app.run(debug=True)