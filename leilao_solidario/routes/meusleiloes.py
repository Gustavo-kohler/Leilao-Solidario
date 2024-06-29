from flask import Blueprint, render_template, redirect, url_for, current_app
from flask_login import current_user, login_required
from leilao_solidario.extensions import db
from leilao_solidario.models import Leilao, Usuario, UsuarioRelLeilao
import os


LEILOES_BP = Blueprint('meusleiloes', __name__, url_prefix='/meusleiloes')

def pegar_imagem(leilao_id):
    imagens_dir = os.path.join(current_app.root_path, 'static/imagens_leilao')
    imagens = os.listdir(imagens_dir)

    for imagem in imagens:
        if imagem.split('_')[0] == leilao_id:
            return os.path.join('static/imagens_leilao', imagem)
    return None

@LEILOES_BP.route('/')
@login_required
def meusleiloes():
    return render_template('meusleiloes.html', current_user=current_user, origin=True)


@LEILOES_BP.route('/leiloes-ativos')
@login_required
def leiloes_ativos():

    leiloes = db.session.query(Leilao).filter_by(status="active").join(UsuarioRelLeilao)\
        .filter(UsuarioRelLeilao.id_usuario == current_user.id).all()

    leiloes_dict = [leilao.to_dict() for leilao in leiloes]

    for leilao in leiloes_dict:
        leilao['imagem'] = pegar_imagem(leilao['id'])
        leilao['imagem'] = '../' + leilao['imagem']

    return render_template('leiloes_ativos.html', current_user=current_user, leiloes=leiloes_dict)


@LEILOES_BP.route('/leiloes-finalizados')
@login_required
def leiloes_finalizados():

    leiloes = db.session.query(Leilao).filter_by(status="ended").join(UsuarioRelLeilao)\
        .filter(UsuarioRelLeilao.id_usuario == current_user.id).all()

    leiloes_dict = [leilao.to_dict() for leilao in leiloes]

    for leilao in leiloes_dict:
        leilao['imagem'] = pegar_imagem(leilao['id'])
        leilao['imagem'] = '../' + leilao['imagem']

    return render_template('leiloes_finalizados.html', current_user=current_user, leiloes=leiloes_dict)


@LEILOES_BP.route('/meusleiloes-ativos')
@login_required
def meusleiloes_ativos():
    leiloes = Leilao.query.filter_by(host=current_user.get_id()).filter_by(status="active").all()

    leiloes_dict = [leilao.to_dict() for leilao in leiloes]

    for leilao in leiloes_dict:
        leilao['imagem'] = pegar_imagem(leilao['id'])
        leilao['imagem'] = '../' + leilao['imagem']

    return render_template('meusleiloes_ativos.html', current_user=current_user, leiloes=leiloes_dict)


@LEILOES_BP.route('/meusleiloes-finalizados')
@login_required
def meusleiloes_finalizados():
    leiloes = Leilao.query.filter_by(host=current_user.get_id()).filter_by(status="ended").all()

    leiloes_dict = [leilao.to_dict() for leilao in leiloes]

    for leilao in leiloes_dict:
        leilao['imagem'] = pegar_imagem(leilao['id'])
        leilao['imagem'] = '../' + leilao['imagem']

    return render_template('meusleiloes_finalizados.html', current_user=current_user, leiloes=leiloes_dict)