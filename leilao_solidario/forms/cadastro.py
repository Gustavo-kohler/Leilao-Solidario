from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length


class FormCadastroLeilao(FlaskForm):
    titulo = StringField('', validators=[DataRequired(), length(min=2, max=40)])
    descricao = StringField('', validators=[DataRequired(), length(min=2, max=100)])
    organizacao = StringField('', validators=[DataRequired(), length(min=2, max=40)])
    imagem = FileField('', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    botao_submit = SubmitField('Cadastrar leilão')
