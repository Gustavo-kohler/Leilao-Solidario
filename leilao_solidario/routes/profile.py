from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from leilao_solidario.extensions import db
from leilao_solidario.models import Usuario
from leilao_solidario.forms.profile import FormAlterarDados

PROFILE = Blueprint('profile', __name__)


@PROFILE.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    forms = FormAlterarDados()
    user = Usuario.query.get(current_user.get_id())
    if forms.validate_on_submit():
        verifica_alteracao = False
        if forms.username.data != '':
            user.username = forms.username.data
            verifica_alteracao = True
        if forms.email.data != '':
            user.email = forms.email.data
            verifica_alteracao = True
        if forms.telefone.data != '':
            user.telefone = forms.telefone.data
            verifica_alteracao = True
        if verifica_alteracao:
            db.session.commit()
            flash(f'{user.username}, seus dados foram alterados.', 'alert-success')
            return redirect(url_for('home.home'))
    
    user_dict = user.to_dict()
    return render_template('profile.html', forms_alteracao=forms, user=user_dict)
