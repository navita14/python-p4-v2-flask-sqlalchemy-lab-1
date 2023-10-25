# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True #true:no new lines when sending json data. if false it will compact all the data without new lines

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here

@app.route('/earthquakes/<int:id>')
def earthquakes_by_id(id):
    #query db for earthquake object 
    eq1 = Earthquake.query.filter(Earthquake.id == id).first()

    if eq1 is None:
        return make_response({"message": f'Eartquake {id} not found.', 404})

    #turn object into dictionary into json
    body = jsonify(eq1.to_dict())
    #return response with body and status code
    return make_response(body, 200)


@app.route('/earthquakes/magnitute/<float:magnitude>')
def get_by_magnitude(magnitude):
    #query db for all mathcing obects
    earthq = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    body = {
        'count' : len(earthq)
    }
    #turned each object into list
    quakes = []
    for e in earthq:
        quakes.append(e.to_dict())
        #add quakess list to the body under the key 'quakes'
        body['quakes'] = quakes
        #return list of dicts in the response
    return make_response(body, 200)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
