

class Config:
    SECRET_KEY = 'gk527tbwv6n'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///leilao_solidario.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'contato@leilao_solidario.com.br'
    MAIL_PASSWORD = 'gk527tbwv6n'
