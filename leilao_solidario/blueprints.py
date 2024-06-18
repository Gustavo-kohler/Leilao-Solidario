def registrar_blueprints(app):
    from .routes.home import HOME
    app.register_blueprint(HOME)

    from .routes.auction import AUCTION
    app.register_blueprint(AUCTION)

    from .routes.leilao import LEILAO
    app.register_blueprint(LEILAO)

    from .routes.cadastro_leilao import CADASTRO_LEILAO
    app.register_blueprint(CADASTRO_LEILAO)