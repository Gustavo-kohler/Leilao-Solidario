from leilao_solidario import db
from leilao_solidario.models import Usuario, Leilao
from app import app
from datetime import datetime


def reset_db():
    with app.app_context():
        db.create_all()

def add_admin_user():
    with app.app_context():
        admin = Usuario(username="admin", email="admin@gmail.com", senha="$2b$12$5YmtHAJ0KJ2rpMV4QsmQUO.hEtB6ved9oM0BgcbfhnaSgrRildWm6", permissao="administrador")
        db.session.add(admin)
        db.session.commit()

def add_exemplo_leiloes():
    with app.app_context():
        # Criar usuários
        usuario1 = Usuario(username="usuario1", email="usuario3@example.com", senha="$2b$12$5YmtHAJ0KJ2rpMV4QsmQUO.hEtB6ved9oM0BgcbfhnaSgrRildWm6")
        usuario2 = Usuario(username="usuario2", email="usuario4@example.com", senha="$2b$12$5YmtHAJ0KJ2rpMV4QsmQUO.hEtB6ved9oM0BgcbfhnaSgrRildWm6")

        db.session.add(usuario1)
        db.session.add(usuario2)
        db.session.commit()

        # Adicionar leilões
        leilao1 = Leilao(
            titulo="Leilão de Arte",
            descricao="Leilão de uma bela pintura",
            organizacao="Galeria de Arte",
            lance_atual=100,
            ultimo=usuario1.id,
            host=usuario2.id,
            status="ativo",
            hora_ultimo=datetime.now()
        )

        leilao2 = Leilao(
            titulo="Leilão de Carro",
            descricao="Leilão de um carro clássico",
            organizacao="Concessionária",
            lance_atual=5000,
            ultimo=usuario2.id,
            host=usuario1.id,
            status="ativo",
            hora_ultimo=datetime.now()
        )

        db.session.add(leilao1)
        db.session.add(leilao2)
        db.session.commit()

add_admin_user()
add_exemplo_leiloes()
