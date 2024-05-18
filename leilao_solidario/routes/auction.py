from flask import Blueprint, render_template, abort
from flask_login import current_user

AUCTION = Blueprint('auction', __name__)


@AUCTION.route('/auction')
def auction():
    return render_template('auction.html', current_user=current_user)
