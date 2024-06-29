from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import ValidationError
from leilao_solidario.models import Leilao
from flask_login import current_user

class FormNewBid(FlaskForm):
    lance = FloatField("Novo lance")
    botao_submit_fazer_lance = SubmitField('Fazer novo lance')

class FormCancelAuction(FlaskForm):
    botao_cancelar = SubmitField("Cancelar leilão")
