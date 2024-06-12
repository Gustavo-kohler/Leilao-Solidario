# from flask import Blueprint, render_template, redirect, url_for
# from flask_login import current_user
# from leilao_solidario.extensions import db
# from leilao_solidario.models import Leilao, Usuario
# from leilao_solidario.forms.bid import FormNewBid, FormCancelAuction
#
# AUCTION = Blueprint('auction', __name__)
#
#
# @AUCTION.route('/auction/<auction_id>', methods=["GET", "POST"])
# def auction(auction_id):
#     auction = Leilao.query.get(auction_id)
#     host = Usuario.query.get(auction.host)
#     form_cancela_leilao = FormCancelAuction()
#     form_novo_lance = FormNewBid()
#
#     if form_cancela_leilao.validate_on_submit():
#         auction.status = "canceled"
#         db.session.commit()
#         return redirect(url_for('auction.auction', auction_id=auction_id))
#
#     if form_novo_lance.validate_on_submit():
#         auction.lance_atual = form_novo_lance.lance.data
#         auction.ultimo = current_user
#         db.session.commit()
#         return redirect(url_for('auction.auction', auction_id=auction_id))
#
#     return render_template('auction.html',
#                             current_user=current_user,
#                             auction=auction,
#                             host=host,
#                             form_cancela_leilao=form_cancela_leilao,
#                             form_novo_lance=form_novo_lance)
#
# @AUCTION.route('/meusleiloes')
# def meusleiloes():
#     return render_template('meusleiloes.html', current_user=current_user)
