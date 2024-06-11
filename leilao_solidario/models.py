from leilao_solidario import login_manager
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from leilao_solidario.extensions import db
from datetime import datetime


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(db.Model, UserMixin):
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    email: so.Mapped[str] = so.mapped_column(sa.String, unique=True, nullable=False)
    senha: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    permissao: so.Mapped[str] = so.mapped_column(sa.String, nullable=True, default='visualizador')

class Leilao(db.Model):
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    titulo: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    descricao: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    imagem: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)    # Deixei string pq pensei que é o link da imagem?
    organizacao: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    lance_atual: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False)
    ultimo: so.Mapped[int] = so.mapped_column(sa.Integer, sa.ForeignKey("usuario.id", name="fk_ultimo_usuario"),
                                              nullable=False)
    host: so.Mapped[int] = so.mapped_column(sa.Integer, sa.ForeignKey("usuario.id", name="fk_host"),
                                              nullable=False)
    status: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    hora_ultimo: so.Mapped[datetime] = so.mapped_column(sa.DateTime, nullable=False)

class UsuarioRelLeilao(db.Model):
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    id_usuario: so.Mapped[int] = so.mapped_column(sa.Integer, db.ForeignKey('usuario.id'), nullable=False)
    id_leilao: so.Mapped[int] = so.mapped_column(sa.Integer, db.ForeignKey('leilao.id'), nullable=False)

    