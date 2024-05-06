from leilao_solidario.status_code import STATUS_ERROR, STATUS_SUCCESS, STATUS_UNAUTHORIZED
from flask_login import current_user


def verificar_permissao(funcionalidade):
    pemissoes = {'Cadastro de Cliente': ['editor_cadastro_cliente', 'editor_geral', 'admin'],
                 'Orquestrador': ['editor_orquestrador', 'editor_geral', 'admin'],
                 'Cadastro Rpa': ['admin']}
    if funcionalidade in pemissoes:
        if current_user.permissao in pemissoes[funcionalidade]:
            return {'STATUS': STATUS_SUCCESS,
                    'MESSAGE': 'Permissão concedida!'}
        else:
            return {'STATUS': STATUS_UNAUTHORIZED,
                    'MESSAGE': 'Você não tem permissão para acessar esta página! Solicite acesso em "Meu Perfil" no canto superior direito.'}
    else:
        return {'STATUS': STATUS_ERROR,
                'MESSAGE': 'Funcionalidade não encontrada!'}
