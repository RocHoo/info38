from redis import StrictRedis


class Config():
    SQLALCHEMY_DATABASE_URI = 'mysql://roou:mysql@localhost/info_python38'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'fE/S+iP1yeXBfEKRIL9mYCubw4AV6InrpByVbSPuz4L6MBANFL4DMg=='

    SESSION_TYPE = 'redis'

    SESSION_REDIS = StrictRedis(host='127.0.0.1', port=6379)

    SESSION_USER_SINGER = True

    SESSION_PERMENENT_LIFETIME = 86400


class DevelopmentConfig(Config):
    DEBUG=True

class ProductionConfig(Config):
    DEBUG=False

config_dict={
    'development':DevelopmentConfig,
    'production':ProductionConfig
}