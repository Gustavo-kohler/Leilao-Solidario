from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField


class FormNewBid(FlaskForm):
    lance = FloatField("Novo lance")
    botao_submit_fazer_lance = SubmitField('Fazer novo lance')


class FormCancelAuction(FlaskForm):
    botao_cancelar = SubmitField("Cancelar leilão")
