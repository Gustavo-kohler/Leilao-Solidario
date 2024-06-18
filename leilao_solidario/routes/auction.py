from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from flask_login import current_user, login_required
from leilao_solidario.extensions import db
from leilao_solidario.models import Leilao, Usuario
from leilao_solidario.forms.bid import FormNewBid, FormCancelAuction
import os

AUCTION = Blueprint('auction', __name__)

def pegar_imagem(leilao_id):
    imagens_dir = os.path.join(current_app.root_path, 'static/imagens_leilao')
    imagens = os.listdir(imagens_dir)

    for imagem in imagens:
        if imagem.split('_')[0] == leilao_id:
            return os.path.join('static/imagens_leilao', imagem)
    return None

@AUCTION.route('/auction/<auction_id>', methods=["GET", "POST"])
def auction(auction_id):
    auction = Leilao.query.get(auction_id)
    host = Usuario.query.get(auction.host)
    form_cancela_leilao = FormCancelAuction()
    form_novo_lance = FormNewBid()

    if form_cancela_leilao.validate_on_submit():
        auction.status = "canceled"
        db.session.commit()
        return redirect(url_for('auction.auction', auction_id=auction_id))
    if form_novo_lance.validate_on_submit():
        auction.lance_atual = form_novo_lance.lance.data
        auction.ultimo = current_user
        db.session.commit()
        return redirect(url_for('auction.auction', auction_id=auction_id))

    return render_template('auction.html', current_user=current_user, auction=auction, host=host, form_cancela_leilao=form_cancela_leilao, form_novo_lance=form_novo_lance)

@AUCTION.route('/meusleiloes')
def meusleiloes():
    if not current_user.is_authenticated:
        flash('Você precisa estar logado para acessar essa página.', 'alert-danger')
        return redirect(url_for('home.login'))
    leiloes = Leilao.query.all()
    leiloes_dict = [leilao.to_dict() for leilao in leiloes if leilao.host == current_user.id]

    for leilao in leiloes_dict:
        leilao['imagem'] = pegar_imagem(leilao['id'])

    return render_template('meusleiloes.html', current_user=current_user, leiloes=leiloes_dict)
