from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
from flask import Flask, jsonify

# Create the SQLAlchemy instance
db = SQLAlchemy()

# Initialize the Flask app with the SQLAlchemy instance
def initialize_app(app):
    db.init_app(app)


app = Flask(__name__)
# db = SQLAlchemy(app)


class Country(db.Model):
    __tablename__ = 'World'  # Replace with your actual table name

    Country = db.Column(db.String(255), primary_key=True)
    Region = db.Column(db.String(255))
    Population = db.Column(db.Integer)
    Area_sq_mi = db.Column(db.Integer)
    Pop_Density_per_sq_mi = db.Column(db.Float)
    Coastline_coast_area_ratio = db.Column(db.Float)
    Net_migration = db.Column(db.Float)
    Infant_mortality_per_1000_births = db.Column(db.Float)
    GDP_per_capita = db.Column(db.Integer)
    Literacy = db.Column(db.Float)
    Phones_per_1000 = db.Column(db.Float)
    Arable = db.Column(db.Float)
    Crops = db.Column(db.Float)
    Other = db.Column(db.Float)
    Climate = db.Column(db.Float)
    Birthrate = db.Column(db.Float)
    Deathrate = db.Column(db.Float)
    Agriculture = db.Column(db.Float)
    Industry = db.Column(db.Float)
    Service = db.Column(db.Float)

class Energy(db.Model):
    __tablename__ = 'Country'

    Country = db.Column(db.String(255), primary_key=True)
    Coal = db.Column(db.Float)
    Gas = db.Column(db.Float)
    Oil = db.Column(db.Float)
    Hydro = db.Column(db.Float)
    Renewable = db.Column(db.Float)
    Nuclear = db.Column(db.Float)

