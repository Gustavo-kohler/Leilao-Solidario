def registrar_blueprints(app):
    from .routes.home import HOME
    app.register_blueprint(HOME)

    from .routes.auction import AUCTION
    app.register_blueprint(AUCTION)
    
    from .routes.meusleiloes import LEILOES_BP
    app.register_blueprint(LEILOES_BP)