from leilao_solidario import login_manager
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from leilao_solidario.extensions import db


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(db.Model, UserMixin):
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    email: so.Mapped[str] = so.mapped_column(sa.String, unique=True, nullable=False)
    senha: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    permissao: so.Mapped[str] = so.mapped_column(sa.String, nullable=True, default='visualizador')
