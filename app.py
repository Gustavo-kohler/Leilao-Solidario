from leilao_solidario import create_app
from leilao_solidario.extensions import db

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
