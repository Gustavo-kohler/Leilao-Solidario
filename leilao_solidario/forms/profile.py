from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError, Optional
from leilao_solidario.models import Usuario


class FormAlterarDados(FlaskForm):
    username = StringField('Nome Completo', validators=[Optional(), length(min=2, max=20)], render_kw={"placeholder": "Informe seu nome"})
    email = StringField('Email', validators=[Optional(), Email()], render_kw={"placeholder": "exemplo@exemplo.com"})
    telefone = StringField('Telefone', validators=[Optional()], render_kw={"placeholder": "(xx)x xxxx-xxxx"})
    botao_submit_alterar_dados = SubmitField('Alterar Dados')


