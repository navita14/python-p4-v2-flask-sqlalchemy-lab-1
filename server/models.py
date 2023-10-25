from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata) #sending a configuration to oyur sqlaclhemy

# Add models here
class Earthquake(db.Model,SerializerMixin): #takes a python object and convert it to a dict. 
    __tablename__ = 'earthquakes'
    id = db.Column(db.Integer, primary_key= True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String) #put() when you want to put how many characters in a string or int
    year = db.Column(db.Integer) #can use DateTime

    def __repr__(self):
        return f'<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>'