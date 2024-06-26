from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError, Optional
from leilao_solidario.models import Usuario


class FormAlterarDados(FlaskForm):
    username = StringField('Nome Completo', validators=[Optional(), length(min=2, max=20)])
    email = StringField('Email', validators=[Optional(), Email()])
    telefone = StringField('Telefone', validators=[Optional()])
    botao_submit_alterar_dados = SubmitField('Alterar Dados')


