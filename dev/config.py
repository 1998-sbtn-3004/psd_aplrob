import os

class BaseConfig:
    # Von außerhalb setzen (docker oder kubernetes)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    pass

def get_config():
    env = os.environ.get('FLASK_ENV', 'development').lower()

    if env == 'production':
        return ProductionConfig
    
    return DevelopmentConfig