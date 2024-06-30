import os
import secrets
from leilao_solidario.models import Usuario, Leilao
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from leilao_solidario.forms.cadastro import FormCadastroLeilao
from leilao_solidario.extensions import bcrypt, db, mail
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
import uuid
from random import randint


CADASTRO_LEILAO = Blueprint('cadastro_leilao', __name__)


def salvar_imagem(form_imagem, id):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_imagem.filename)
    imagem_fn = f"{id}_{random_hex}{f_ext}"
    imagem_path = os.path.join(current_app.root_path, 'static/imagens_leilao', imagem_fn)
    form_imagem.save(imagem_path)
    return imagem_fn


@CADASTRO_LEILAO.route('/cadastro_leilao', methods=['GET', 'POST'])
@login_required
def cadastrar_leilao():
    form_cadastro_leilao = FormCadastroLeilao()
    if not current_user.is_authenticated:
        flash('Você precisa estar logado para acessar essa página.', 'alert-danger')
        return redirect(url_for('home.login'))
    if form_cadastro_leilao.validate_on_submit():
        id = uuid.uuid4().hex[:8]
        if form_cadastro_leilao.imagem.data:
            salvar_imagem(form_cadastro_leilao.imagem.data, id)

        leilao = Leilao(
            id=id,
            titulo=form_cadastro_leilao.titulo.data,
            descricao=form_cadastro_leilao.descricao.data,
            organizacao=form_cadastro_leilao.organizacao.data,
            lance_atual=0,
            host=current_user.id,
            ultimo=None,
            status='active',
            hora_ultimo=datetime.now(),
            numero_secreto=randint(10000000, 99999999)
        )
        db.session.add(leilao)
        db.session.commit()
        flash('Leilão cadastrado com sucesso!', 'alert-success')
        return redirect(url_for('home.home'))
    return render_template('cadastro_leilao.html', form_cadastro_leilao=form_cadastro_leilao)
