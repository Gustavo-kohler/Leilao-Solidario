from flask import Flask
from leilao_solidario.status_code import STATUS_ERROR, STATUS_SUCCESS, STATUS_UNAUTHORIZED, STATUS_NO_MODIFICATION
from .extensions import db, login_manager, bcrypt, mail
from .blueprints import registrar_blueprints
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.static_folder = 'static'
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    registrar_blueprints(app)
    return app


