from flask import Blueprint, render_template, abort

AUCTION = Blueprint('auction', __name__)


@AUCTION.route('/auction')
def auction():
    return render_template('auction.html')
