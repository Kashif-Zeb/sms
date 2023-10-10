from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from project.app.db import db
from project.blueprints.student import bp as student
from project.blueprints.department import bp as department
from project.blueprints.course import bp as course
from project import config
import os


def create_app():
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testing.db"
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mysql+pymysql://{config.DB_USER}:{config.DB_PWD}@{config.DB_URL}:{config.DB_PORT}/{config.DB_NAME}"
    # app.config[
    #     "SQLALCHEMY_DATABASE_URI"
    # ] = "mysql+pymysql://root:kashif@localhost:3306/sms"

    db.init_app(app)
    app.config[
        "JWT_SECRET_KEY"
    ] = "60b8b427938bc9f2fbe65d98640e831b4a8522f56150b97f141677d02570819b"
    jwt = JWTManager(app)

    @app.errorhandler(422)
    def webargs_error_handler(err):
        headers = err.data.get("headers", None)
        messages = err.data.get("messages", ["Invalid request."])
        if headers:
            return jsonify({"errors": messages}), err.code, headers
        else:
            return jsonify({"errors": messages}), err.code

    # with app.app_context():
    #     db.create_all()
    app.register_blueprint(student)
    app.register_blueprint(department)
    app.register_blueprint(course)
    return app
