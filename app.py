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


# @app.route('/api/sample_country_data')
# def sample_country_data():
#     data = Country.query.limit(10).all()
#     result = [{
#         'Country': country.Country,
#         'Population': country.Population,
#         'Area_sq_mi': country.Area_sq_mi,
#         'Pop_Density_per_sq_mi': country.Pop_Density_per_sq_mi,
#         'Coastline_coast_area_ratio': country.Coastline_coast_area_ratio,
#         'Net_migration': country.Net_migration,
#         'Infant_mortality_per_1000_births': country.Infant_mortality_per_1000_births,
#         'GDP_per_capita': country.GDP_per_capita,
#         'Literacy': country.Literacy,
#         'Phones_per_1000': country.Phones_per_1000,
#         'Arable': country.Arable,
#         'Crops': country.Crops,
#         'Other': country.Other,
#         'Climate': country.Climate,
#         'Birthrate': country.Birthrate,
#         'Deathrate': country.Deathrate,
#         'Agriculture': country.Agriculture,
#         'Industry': country.Industry,
#         'Service': country.Service
#     } for country in data]
#     return jsonify(result)

# Route for the dashboard page
# Route for countries with the highest literacy rates
@app.route('/highest_literacy_countries')
def highest_literacy_countries_chart():
    result = Country.query.order_by(Country.Literacy.desc()).limit(5).all()
    data = [{'Country': country.Country, 'Literacy': country.Literacy} for country in result]
    return jsonify({'status': 'success', 'data': data})
# initialize_app(app)

# Example route for countries with the highest literacy rates
# @app.route('/highest_literacy_countries')
# def highest_literacy_countries():
#     try:
#         # Query the data using SQLAlchemy's order_by and limit
#         result = Country.query.order_by(Country.Literacy.desc()).limit(5).all()

#         # Prepare JSON response
#         data = [
#             {'Country': country.Country, 'Literacy': country.Literacy}
#             for country in result
#         ]

#         # Return the data as JSON
#         return jsonify({'status': 'success', 'data': data})

#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)})

# # route for countries with the lowest literacy rates
# @app.route('/lowest_literacy_countries')
# def lowest_literacy_countries():
#     try:
#         # Query the data using SQLAlchemy's order_by and limit
#         result = Country.query.order_by(Country.Literacy).limit(5).all()

#         # Prepare JSON response
#         data = [
#             {'Country': country.Country, 'Literacy': country.Literacy}
#             for country in result
#         ]

#         # Return the data as JSON
#         return jsonify({'status': 'success', 'data': data})

#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)})

# # route for countries with the highest net migration
# @app.route('/highest_net_migration_countries')
# def highest_net_migration_countries():
#     try:
#         # Query the data using SQLAlchemy's order_by and limit
#         result = Country.query.order_by(Country.Net_migration.desc()).limit(5).all()

#         # Prepare JSON response
#         data = [
#             {'Country': country.Country, 'Net_migration': country.Net_migration}
#             for country in result
#         ]

#         # Return the data as JSON
#         return jsonify({'status': 'success', 'data': data})

#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)})

# # route for regions with the highest GDP per capita (limited to top 10)
# @app.route('/highest_gdp_per_capita_regions')
# def highest_gdp_per_capita_regions():
#     try:
#         # Query the data using SQLAlchemy's order_by, group_by, func.max, and limit
#         result = (
#             db.session.query(Country.Region, func.max(Country.GDP_per_capita))
#             .group_by(Country.Region)
#             .order_by(func.max(Country.GDP_per_capita).desc())
#             .limit(10)  # Limit the results to top 10
#             .all()
#         )

#         # Prepare JSON response
#         data = [
#             {'Region': row[0], 'Highest_GDP_per_capita': row[1]}
#             for row in result
#         ]

#         # Return the data as JSON
#         return jsonify({'status': 'success', 'data': data})

#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)})

# # Example route for countries with the lowest birthrates
# @app.route('/lowest_birthrate_countries')
# def lowest_birthrate_countries():
#     try:
#         # Query the data using SQLAlchemy's order_by and limit
#         result = db.session.query(Country.Country, Country.Birthrate).order_by(Country.Birthrate).limit(5).all()

#         # Prepare JSON response
#         data = [
#             {'Country': row[0], 'Birthrate': row[1]}
#             for row in result
#         ]

#         # Return the data as JSON
#         return jsonify({'status': 'success', 'data': data})

#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)})

# # Additional routes can be added based on your requirements



    
    

# @app.route('/highest_coal_consumption_regions')
# def highest_coal_consumption_regions():
#     try:
#         # Query the data using SQLAlchemy's order_by, group_by, func.max, and limit
#         result = (
#             db.session.query(Energy.Country, func.max(Energy.Coal))
#             .group_by(Energy.Country)
#             .order_by(func.max(Energy.Coal).desc())
#             .limit(10)  # Limit the results to top 10
#             .all()
#         )

#         # Prepare JSON response
#         data = [
#             {'Country': row[0], 'Highest_Coal_Consumption': row[1]}
#             for row in result
#         ]

#         # Return the data as JSON
#         return jsonify({'status': 'success', 'data': data})

#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)})

# # ...

# # Example route for regions with the highest Nuclear energy consumption (limited to top 10)
# @app.route('/highest_nuclear_consumption_regions')
# def highest_nuclear_consumption_regions():
#     try:
#         # Query the data using SQLAlchemy's order_by, group_by, func.max, and limit
#         result = (
#             db.session.query(Energy.Country, func.max(Energy.Nuclear))
#             .group_by(Energy.Country)
#             .order_by(func.max(Energy.Nuclear).desc())
#             .limit(10)  # Limit the results to top 10
#             .all()
#         )

#         # Prepare JSON response
#         data = [
#             {'Country': row[0], 'Highest_Nuclear_Consumption': row[1]}
#             for row in result
#         ]

#         # Return the data as JSON
#         return jsonify({'status': 'success', 'data': data})

#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)})




# @app.route('/api/sample_country_data')
# def sample_country_data():
#     data = Country.query.limit(10).all()  # adjust as needed
#     result = [{
#         'Country': country.Country,
#         'Population': country.Population,
#         'Population': country.Population,
#         'Area_sq_mi': country.Area_sq_mi,
#         'Pop_Density_per_sq_mi': country.Pop_Density_per_sq_mi,
#         'Coastline_coast_area_ratio': country.Coastline_coast_area_ratio,
#         'Net_migration': country.Net_migration,
#         'Infant_mortality_per_1000_births': country.Infant_mortality_per_1000_births,
#         'GDP_per_capita': country.GDP_per_capita,
#         'Literacy': country.Literacy,
#         'Phones_per_1000': country.Phones_per_1000,
#         'Arable': country.Arable,
#         'Crops': country.Crops,
#         'Other': country.Other,
#         'Climate': country.Climate,
#         'Birthrate': country.Birthrate,
#         'Deathrate': country.Deathrate,
#         'Agriculture': country.Agriculture,
#         'Industry': country.Industry,
#         'Service': country.Service
#     }
#     for country in data]
#         # ... add other fields
#     # } for item in data]
#     return jsonify(result)

# @app.route('/sample_energy_data')
# def sample_energy_data():
#     try:
#         # Query sample data (e.g., first 5 records)
#         sample_data = Energy.query.limit(5).all()

#         # Prepare JSON response
#         data = [
#             {
#                 'Country': row.Country,
#                 'Coal': row.Coal,
#                 'Gas': row.Gas,
#                 'Oil': row.Oil,
#                 'Hydro': row.Hydro,
#                 'Renewable': row.Renewable,
#                 'Nuclear': row.Nuclear,
#             }
#             for row in sample_data
#         ]

#         return jsonify({'status': 'success', 'message': 'Sample energy data retrieved successfully', 'data': data})

#     except Exception as e:
#         return jsonify({'status': 'error', 'message': f'Error retrieving sample energy data: {str(e)}'})


# @app.route('/dashboard')
# def dashboard():
#     return render_template('index.html')

if __name__ == '__main__':
    test_db_connection()  # Call this function here
    app.run(debug=True)