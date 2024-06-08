from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import ValidationError
from leilao_solidario.models import Leilao
from flask_login import current_user

class FormNewBid(FlaskForm):
    lance = FloatField("Novo lance")
    user = current_user.id 
    botao_submit_fazer_lance = SubmitField('Fazer novo lance')

    def validate_bid(self, lance, auction):
        if lance <= auction.lance_atual:
            raise ValidationError('Lance mais baixo que o atual.')
        
    def validate_user(self, user, auction):
        if user == auction.ultimo:
            raise ValidationError("Voce fez o ultimo lance")
    
class FormCancelAuction(FlaskForm):
    botao_cancelar = SubmitField("Cancelar leilão")
