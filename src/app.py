"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet, Personaje, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#ENDPOINTS 
#Esto trae todos los personajes 
@app.route('/personaje', methods=['GET'])
def traer_todos_personaje():
    personaje = Personaje.query.all()
    results = list(map(lambda item: item.serialize(),personaje))
    print(personaje)
    response_body = {
        "msg": "Hello, this is your GET all characters response ",
        "personajes": results
    }
#Esto trae un solo personaje
@app.route('/personaje/<int:personaje_id>', methods=['GET'])
def traer_solo_personaje(personaje_id):
    personaje = Personaje.query.filter_by(id=personaje_id).first()
    response_body = {
        "msg": "Hello, this is your GET 1 character response ",
         "results":personaje.serialize()
    }
    return jsonify(response_body), 200

#Esto trae todos los planetas
@app.route('/planeta', methods=['GET'])
def traer_todos_planetas():
    planeta = Planet.query.all()
    results = list(map(lambda item: item.serialize(),planeta))
    response_body = {
        "msg": "Hello, this is your GET all Planets response ",
        "planetas": results
    }
    return jsonify(response_body), 200

#Esto trae un planeta concreto
@app.route('/planeta/<int:planeta_id>', methods=['GET'])
def traer_solo_planeta(planeta_id):
    planeta = Planet.query.filter_by(id=planeta_id).first()
    response_body = {
        "msg": "Hello, this is your GET 1 planet response ",
        "results":planeta.serialize()
    }
    return jsonify(response_body), 200

#Esto trae todos los usuarios
@app.route('/users', methods=['GET'])
def handle_user():
    usuarios = User.query.all()
    results = list(map(lambda item: item.serialize(),usuarios))
    response_body = {
        "msg": "Hello, this is your GET  ALL users response ",
        "results": results
    }
    return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
