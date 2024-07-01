from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import length, Email, Optional


class FormAlterarDados(FlaskForm):
    username = StringField('Nome', validators=[Optional(), length(min=2, max=20)], render_kw={"placeholder": "Informe seu nome"})
    email = StringField('Email', validators=[Optional(), Email()], render_kw={"placeholder": "exemplo@exemplo.com"})
    telefone = StringField('Telefone', validators=[Optional()], render_kw={"placeholder": "(xx)x xxxx-xxxx"})
    botao_submit_alterar_dados = SubmitField('Alterar Dados')
