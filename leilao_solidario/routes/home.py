from leilao_solidario.models.user import Usuario
from flask import Blueprint, render_template, redirect, url_for, flash, request
from leilao_solidario.forms.login import FormLogin, FormCriarConta
from leilao_solidario.extensions import bcrypt, db, mail
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message


HOME = Blueprint('home', __name__)


@HOME.route('/')
def home():
    return render_template('home.html')


@HOME.route('/login', methods=['GET','POST'])
def login():
    form_login = FormLogin()
    form_criar_conta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if not usuario:
            flash(f'Não há conta cadastrada com o email: {form_login.email.data}.', 'alert-danger')
        else:
            if bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
                login_user(usuario, remember=form_login.lembrar_dados.data)
                flash(f'Seja bem-vindo {usuario.username}!', 'alert-success')
                par_next = request.args.get('next')
                if par_next:
                    return redirect(par_next)
                return redirect(url_for('home.home'))
            else:
                flash(f'Senha incorreta, tente novamente.', 'alert-danger')

    if form_criar_conta.validate_on_submit() and 'botao_submit_criar_conta' in request.form:
        senha_criptografada = bcrypt.generate_password_hash(form_criar_conta.senha.data).decode('utf-8')
        usuario = Usuario(username=form_criar_conta.username.data,
                          email=form_criar_conta.email.data,
                          senha=senha_criptografada)
        db.session.add(usuario)
        db.session.commit()
        flash(
            f'Sua conta com o email "{form_criar_conta.email.data}" foi criada com sucesso! Faça login para entrar na plataforma.',
            'alert-success')
        return redirect(url_for('home.login'))
    return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta)


@HOME.route('/sair')
@login_required
def sair():
    logout_user()
    flash('Logout feito com sucesso!', 'alert-success')
    return redirect(url_for('home.home'))


@HOME.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html')
