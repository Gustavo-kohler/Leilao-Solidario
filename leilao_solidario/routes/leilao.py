from leilao_solidario.models import Usuario, Leilao
from flask import Blueprint, render_template, current_app
from flask_login import current_user, logout_user, login_required
import os


LEILAO = Blueprint('leilao', __name__)


def pegar_imagem(leilao_id):
    imagens_dir = os.path.join(current_app.root_path, 'static/imagens_leilao')
    imagens = os.listdir(imagens_dir)

    for imagem in imagens:
        if imagem.split('_')[0] == leilao_id:
            return os.path.join('static/imagens_leilao', imagem)
    return None


@LEILAO.route('/leiloes')
@login_required
def lista_leiloes():
    leiloes = Leilao.query.filter_by(status='active')
    leiloes_dict = [leilao.to_dict() for leilao in leiloes if leilao.host != current_user.id]

    for leilao in leiloes_dict:
        if leilao['ultimo']:
            leilao['ultimo'] = Usuario.query.get(leilao['ultimo']).username
        else:
            leilao['ultimo'] = 'Nenhum'
        leilao['host'] = Usuario.query.get(leilao['host']).username
        leilao['imagem'] = pegar_imagem(leilao['id'])
        print(leilao['imagem'])
    return render_template('lista_leiloes.html', leiloes=leiloes_dict)

