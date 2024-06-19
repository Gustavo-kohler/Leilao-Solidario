from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from leilao_solidario.extensions import db
from leilao_solidario.models import Leilao, Usuario, UsuarioRelLeilao


LEILOES_BP = Blueprint('meusleiloes', __name__, url_prefix='/meusleiloes')


@LEILOES_BP.route('/')
@login_required
def meusleiloes():

    return render_template('meusleiloes.html', current_user=current_user)


@LEILOES_BP.route('/leiloes-que-participo')
@login_required
def leiloes_que_participo():

    leiloes = db.session.query(Leilao).join(UsuarioRelLeilao).filter(UsuarioRelLeilao.id_usuario == current_user.id).all()

    return render_template('leiloes_que_participo.html', current_user=current_user, leiloes=leiloes)


@LEILOES_BP.route('/leiloes-ativos')
@login_required
def leiloes_ativos():

    leiloes = db.session.query(Leilao).join(UsuarioRelLeilao).filter(UsuarioRelLeilao.id_usuario == current_user.id).all()

    return render_template('leiloes_ativos.html', current_user=current_user, leiloes=leiloes)


@LEILOES_BP.route('/leiloes-finalizados')
@login_required
def leiloes_finalizados():

    leiloes = db.session.query(Leilao).join(UsuarioRelLeilao).filter(UsuarioRelLeilao.id_usuario == current_user.id).all()

    return render_template('leiloes_finalizados.html', current_user=current_user, leiloes=leiloes)