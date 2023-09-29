from flask import Flask, jsonify
from project.app.db import db
from project.blueprints.student import bp as student
from project.blueprints.department import bp as department


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testing.db"

    db.init_app(app)

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
    return app
