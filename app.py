from sqlalchemy import func
from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import os


from models import db, Country, Energy, initialize_app
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# # Define your config variables with default values
server = os.environ.get('server')
database = os.environ.get('database')
username = os.environ.get('username')
password = os.environ.get('password')


#SQL Server connection settings
# server = 'WIN-LJ7C2L79T2K'
# database = 'Countries'
# username = 'sa'
# password = 'MontRouge88#'



app = Flask(__name__)



# Create the SQLAlchemy engine
engine = create_engine(f"mssql+pymssql://{username}:{password}@{server}/{database}")

# Set up the Flask app with SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pymssql://{username}:{password}@{server}/{database}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
initialize_app(app)

# with app.app_context():
#     db.create_all()


# Function to test database connection
def test_db_connection():
    with app.app_context():
        try:
            connection = db.engine.connect()
            print("Connection successful!")
            connection.close()
        except Exception as e:
            print(f"Connection failed: {e}")


# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')    


# Route for the sample country data
@app.route('/api/sample_country_data')
def sample_country_data():
    try:
        data = Country.query.limit(10).all()
        result = [
            {
                'Country': country.Country,
                'Population': country.Population,
                'Area_sq_mi': country.Area_sq_mi,
                'Pop_Density_per_sq_mi': country.Pop_Density_per_sq_mi,
                'Coastline_coast_area_ratio': country.Coastline_coast_area_ratio,
                'Net_migration': country.Net_migration,
                'Infant_mortality_per_1000_births': country.Infant_mortality_per_1000_births,
                'GDP_per_capita': country.GDP_per_capita,
                'Literacy': country.Literacy,
                'Phones_per_1000': country.Phones_per_1000,
                'Arable': country.Arable,
                'Crops': country.Crops,
                'Other': country.Other,
                'Climate': country.Climate,
                'Birthrate': country.Birthrate,
                'Deathrate': country.Deathrate,
                'Agriculture': country.Agriculture,
                'Industry': country.Industry,
                'Service': country.Service
            }
            for country in data
        ]
        return jsonify(result)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Route for the dashboard page
@app.route('/dashboard')
def dashboard_page():
    try:
        # Fetch data for visualization (you can modify this query as needed)
        data = Country.query.limit(10).all()
        return render_template('dashboard.html', data=data)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
    
# # Route for countries with the highest literacy rates
@app.route('/highest_literacy_countries')
def highest_literacy_countries():
    result = Country.query.order_by(Country.Literacy.desc()).limit(5).all()
    data = [{'Country': country.Country, 'Literacy': country.Literacy} for country in result]
    return jsonify({'status': 'success', 'data': data})


