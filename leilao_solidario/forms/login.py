from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError
from leilao_solidario.models import Usuario


class FormCriarConta(FlaskForm):
    username = StringField(
        'Nome de Usuário',
        validators=[
           DataRequired(message='O nome de usuário é obrigatório.'),
           length(min=2, max=20, message='O nome de usuário deve ter de 2 a 20 caracteres.')
        ]
    )

    email = StringField(
        'Email',
        validators=[
            DataRequired(message='O email é obrigatório.'),
            Email(message='Formato de email inválido.')
        ]
    )

    telefone = StringField(
        'Telefone',
        validators=[
            DataRequired(message='O telefone é obrigatório.')
        ]
    )

    senha = PasswordField(
        'Senha',
        validators=[
            DataRequired(message='A senha é obrigatória.'),
            length(min=6, max=20, message='A senha deve ter de 6 a 20 caracteres.')
        ]
    )

    confirmacao_senha = PasswordField(
        'Confirme a Senha',
        validators=[
            DataRequired(message='A confirmação de senha é obrigatória.'),
            EqualTo('senha', message='As senhas devem ser iguais.')
        ]
    )

    botao_submit_criar_conta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Email já cadastrado! Cadastre-se com outro email ou faça login.')

    def validate_telefone(self, telefone):
        if len(telefone.data) != 11:
            raise ValidationError('Número de dígitos diferente do esperado.')

class FormLogin(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(message='O email é obrigatório.'),
            Email(message='Formato de email inválido.')
        ]
    )

    senha = PasswordField(
        'Senha',
        validators=[
            DataRequired(message='A senha é obrigatória.'),
            length(min=6, max=20, message='A senha deve ter de 6 a 20 caracteres.')
        ]
    )

    lembrar_dados = BooleanField('Lembrar-me')
    botao_submit_login = SubmitField('Fazer Login')
