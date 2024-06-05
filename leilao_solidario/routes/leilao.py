from leilao_solidario.models import Usuario, Leilao
from flask import Blueprint, render_template, redirect, url_for, flash, request
from leilao_solidario.forms.login import FormLogin, FormCriarConta
from leilao_solidario.extensions import bcrypt, db, mail
from flask_login import login_user, current_user, logout_user, login_required


LEILAO = Blueprint('leilao', __name__)


@LEILAO.route('/leiloes')
def lista_leiloes():
    leiloes = Leilao.query.all()
    print(current_user.id)
    leiloes_dict = [leilao.to_dict() for leilao in leiloes if leilao.host != current_user.id]
    for leilao in leiloes_dict:
        leilao['ultimo'] = Usuario.query.get(leilao['ultimo']).username
        leilao['host'] = Usuario.query.get(leilao['host']).username
    return render_template('lista_leiloes.html', leiloes=leiloes_dict)

