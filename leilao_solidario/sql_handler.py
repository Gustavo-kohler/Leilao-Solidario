from leilao_solidario import db
from leilao_solidario.models import Usuario
from app import app

def reset_db():
    with app.app_context():
        db.create_all()

reset_db()
