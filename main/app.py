from flask import Flask
from database.db import db
from database.bcrypt import bcrypt
import os

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    db.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        import models
        db.create_all()

    return app