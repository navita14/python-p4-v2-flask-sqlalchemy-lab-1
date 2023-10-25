# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True 

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/earthquakes/<int:id>') 
def earthquake_with_id(id):
    ertq = Earthquake.query.filter(Earthquake.id == id).first()
    if ertq is None:
        return make_response({'message': f"Earthquake {id} not found."}, 404)

    body = jsonify(ertq.to_dict())
    return body, 200

@app.route('/earthquakes/magnitude/<float:magnitude>') 
def get_by_magnitude(magnitude):
    earthq = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    quakes = []
    for e in earthq:
        quakes.append(e.to_dict())
        
    body = {
    'count' : len(earthq),
    'quakes' : quakes
    }
    
    return make_response(body, 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
