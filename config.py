"""Flask configuration."""

class Config:
    """Base config."""
    SECRET_KEY = 'jhsd]e[3984764.573kjs4a1jkrjg876}][}[[.&6s'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True