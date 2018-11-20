from flask import Flask, Blueprint
from .api.v2 import version2 as v2
from .db_config import create_tables

def create_app():
    app = Flask(__name__)
    app.register_blueprint(v2)
    create_tables()

    return app