def registrar_blueprints(app):
    from .routes.home import HOME
    app.register_blueprint(HOME)

    from .routes.leilao import LEILAO
    app.register_blueprint(LEILAO)
