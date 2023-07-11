from flask import Flask
from .views import main_blueprint


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../flask-forum.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .database import db
    db.init_app(app)

    app.register_blueprint(main_blueprint)

    return app
