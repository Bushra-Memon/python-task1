from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_user = "root"
db_password = ""
db_host = "localhost"
db_name = "activity_db"

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return{
            'id':self.id,
            'name': self.name
        }
with app.app_context():
    db.create_all()

@app.route('/activities', methods=['POST'])
def add_activity():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Name is required'}),400

    activity = Activity(name=name)
    db.session.add(activity)
    db.session.commit()
    return jsonify(activity.to_dict()),201

@app.route('/activities', methods=['GET'])
def get_activities():
    activities = Activity.query.all()
    return jsonify([activity.to_dict() for activity in activities]),200

@app.route('/activities/<int:id>', methods=['GET'])
def get_activity(id):
    activity = Activity.query.get(id)
    if not activity:
        return jsonify({"error":"Activity not found"}),404
    return jsonify(activity.to_dict()),200

@app.route('/activities/<int:id>', methods=['PUT'])
def update_activity(id):
    activity = Activity.query.get(id)
    if not activity:
        return jsonify({"error": "Activity not found"}), 404
    
    data = request.get_json()
    activity.name = data.get("name",activity.name)
    db.session.commit()
    return jsonify(activity.to_dict()), 200

@app.route('/activities/<int:id>', methods=['DELETE'])
def delete_activity(id):
    activity = Activity.query.get(id)
    if not activity:
        return jsonify({"error": "Activity not found"}),404

    db.session.delete(activity)
    db.session.commit()
    return jsonify({"messege": f"Activity {id} deleted..."}),200
    
if __name__ == '__main__':
    app.run(debug=True)

