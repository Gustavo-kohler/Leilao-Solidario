from flask import Blueprint, render_template, redirect, url_for, flash, current_app, request
from flask_login import current_user, login_required
from leilao_solidario.extensions import db
from leilao_solidario.models import Leilao, Usuario, UsuarioRelLeilao
from leilao_solidario.forms.bid import FormNewBid, FormCancelAuction
import os
from datetime import datetime, timedelta

AUCTION = Blueprint('auction', __name__)


def pegar_imagem(leilao_id):
    imagens_dir = os.path.join(current_app.root_path, 'static/imagens_leilao')
    imagens = os.listdir(imagens_dir)

    for imagem in imagens:
        if imagem.split('_')[0] == leilao_id:
            return os.path.join('static/imagens_leilao', imagem)
    return None


@AUCTION.route('/auction/<auction_id>', methods=['GET', 'POST'])
@login_required
def auction(auction_id):
    auction = Leilao.query.get(auction_id)
    imagem = pegar_imagem(auction.id)
    host = Usuario.query.get(auction.host)

    form_cancela_leilao = FormCancelAuction()
    form_novo_lance = FormNewBid()

    duracao_delta_seg = 120

    now = datetime.now()
    time_diff = now - auction.hora_ultimo
    if time_diff.total_seconds() > timedelta(seconds=duracao_delta_seg).total_seconds():
        auction.status = "ended"
        db.session.commit()
        time_left = timedelta(seconds=0)
    else:
        time_left = timedelta(seconds=duracao_delta_seg) - time_diff
    time_left = time_left.total_seconds()

    erro = ''

    if form_novo_lance.validate_on_submit():
        if auction.ultimo == int(current_user.get_id()):
            erro = 'mesmo_user'
        elif auction.lance_atual >= form_novo_lance.lance.data:
            erro = 'lance_menor'
        elif time_diff.total_seconds() > timedelta(seconds=duracao_delta_seg).total_seconds():
            erro = 'acabou_tempo'
        else:
            auction.lance_atual = form_novo_lance.lance.data
            auction.ultimo = current_user.get_id()
            auction.hora_ultimo = now

            exists = UsuarioRelLeilao.query.filter_by(id_usuario=current_user.get_id()).first()
            if not exists:
                relacao_usuario_leilao = UsuarioRelLeilao(id_usuario=current_user.get_id(), id_leilao=auction_id)
                db.session.add(relacao_usuario_leilao)
            db.session.commit()
    elif form_cancela_leilao.validate_on_submit():
        auction.status = "canceled"
        db.session.commit()

    if auction.ultimo is not None:
        ultimo_licitante = Usuario.query.get(auction.ultimo).username
    else:
        ultimo_licitante = Usuario.query.get(auction.ultimo)

    return render_template(
        'auction.html',
        current_user_id=int(current_user.get_id()),
        auction=auction,
        host=host,
        ultimo_licitante=ultimo_licitante,
        form_cancela_leilao=form_cancela_leilao,
        form_novo_lance=form_novo_lance,
        imagem=imagem,
        time_left=time_left,
        erro=erro
    )

@AUCTION.route('/meusleiloes')
@login_required
def meusleiloes():
    if not current_user.is_authenticated:
        flash('Você precisa estar logado para acessar essa página.', 'alert-danger')
        return redirect(url_for('home.login'))
    leiloes = Leilao.query.all()
    leiloes_dict = [leilao.to_dict() for leilao in leiloes if leilao.host == current_user.id]

    for leilao in leiloes_dict:
        leilao['imagem'] = pegar_imagem(leilao['id'])

    return render_template('meusleiloes.html', current_user=current_user, leiloes=leiloes_dict)
