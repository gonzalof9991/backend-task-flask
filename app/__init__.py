import os

from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_smorest import Api
from dotenv import load_dotenv
# Yours
import app.models
# Routes
from app.routes import taskBlueprint, categoryBlueprint, userBlueprint
# DB
from app.connections.db import db


def create_app():
    app = Flask(__name__)
    load_dotenv()
    # Configuración de Flask
    app.config["API_TITLE"] = "Tasks REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    # Configuración DB -> SQLITE
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///data.db")
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/task-bd'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config['SECRET_KEY'] = 'secret!'
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    # Crear todas las tablas de la bd antes de la consulta


    @app.route("/")
    def index():
        return jsonify({"message": "Welcome to the API"})

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({"message": "Page not found"}), 404

    # Registramos las rutas
    api.register_blueprint(taskBlueprint)
    api.register_blueprint(categoryBlueprint)
    api.register_blueprint(userBlueprint)

    return app
