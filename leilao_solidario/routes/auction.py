from flask import Blueprint, render_template, abort
from flask_login import current_user
from leilao_solidario.models import Leilao, Usuario

AUCTION = Blueprint('auction', __name__)


@AUCTION.route('/auction/<auction_id>', methods=["GET", "POST"])
def auction(auction_id):
    auction = Leilao.query.get(auction_id)
    host = Usuario.query.get(auction.host)
    return render_template('auction.html', current_user=current_user, auction=auction, host=host)
