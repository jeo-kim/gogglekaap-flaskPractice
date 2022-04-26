class Config():
    """ flask config """
    SECRET_KEY = 'asdfasdf'
    SESSION_COOKIE_NAME = 'gogglekaap'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/gogglekaap?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_DOC_EXPANSION = 'list'  # swagger가 펼침상태가 됨.


class DevelopmentConfig(Config):
    """ flask config for dev """
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 1
    # todo front 호출시 처리
    WTF_CSRF_ENABLED = False


class ProductionConfig(DevelopmentConfig):
    pass
