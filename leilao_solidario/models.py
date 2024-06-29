from leilao_solidario import login_manager
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from leilao_solidario.extensions import db
from datetime import datetime
import uuid


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(db.Model, UserMixin):
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    telefone: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    email: so.Mapped[str] = so.mapped_column(sa.String, unique=True, nullable=False)
    senha: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'telefone': self.telefone,
            'email': self.email,
            'senha': self.senha
        }


def generate_hex_id():
    return uuid.uuid4().hex[:8]


class Leilao(db.Model):
    id: so.Mapped[str] = so.mapped_column(sa.String, primary_key=True, default=generate_hex_id)
    titulo: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    descricao: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    organizacao: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    lance_atual: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False)
    ultimo: so.Mapped[int] = so.mapped_column(sa.Integer, sa.ForeignKey("usuario.id", name="fk_ultimo_usuario"), nullable=True, default=None)
    host: so.Mapped[int] = so.mapped_column(sa.Integer, sa.ForeignKey("usuario.id", name="fk_host"),nullable=False)
    status: so.Mapped[str] = so.mapped_column(sa.String, nullable=False, default="active")
    hora_ultimo: so.Mapped[datetime] = so.mapped_column(sa.DateTime)
    numero_secreto: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'organizacao': self.organizacao,
            'lance_atual': self.lance_atual,
            'ultimo': self.ultimo,
            'host': self.host,
            'status': self.status,
            'hora_ultimo': self.hora_ultimo.strftime('%H:%M dia (%d/%m/%Y)') if self.hora_ultimo else None,
            'numero_secreto': self.numero_secreto
        }


class UsuarioRelLeilao(db.Model):
    id: so.Mapped[str] = so.mapped_column(sa.String, primary_key=True, default=generate_hex_id)
    id_usuario: so.Mapped[str] = so.mapped_column(sa.String, db.ForeignKey('usuario.id'), nullable=False)
    id_leilao: so.Mapped[str] = so.mapped_column(sa.String, db.ForeignKey('leilao.id'), nullable=False)

    def __repr__(self):
        return f'<UsuarioRelLeilao> {self.id_leilao}'
