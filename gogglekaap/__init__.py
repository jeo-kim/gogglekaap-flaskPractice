from flask import Flask, render_template, g
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    print('run: create_app()')
    app = Flask(__name__)

    from .configs import DevelopmentConfig, ProductionConfig

    if not config:
        if app.config['DEBUG']:
            config = DevelopmentConfig()
        else:
            config = ProductionConfig()

    print("run with: ", config)

    app.config['SECRET_KEY'] = 'asdfasdf'
    app.config['SESSION_COOKIE_NAME'] = 'gogglekaap'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/gogglekaap?charset=utf8'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'  # swagger가 펼침상태가 됨.

    if app.config['DEBUG']:
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
        app.config['WTF_CSRF_ENABLED'] = False

    '''CSRF INIT'''
    csrf.init_app(app)

    ''' DB INIT '''
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    '''Routes INIT'''
    from gogglekaap.routes import base_route, auth_route
    app.register_blueprint(base_route.bp)
    app.register_blueprint(auth_route.bp)

    '''Restx INIT'''
    from gogglekaap.apis import blueprint as api
    app.register_blueprint(api)

    '''REQUEST HOOK'''
    @app.before_request
    def before_request():
        g.db = db.session

    @app.teardown_request
    def teardown_request(exception):
        if hasattr(g, 'db'):
            g.db.close()

    @app.errorhandler(404)
    def page_404(error):
        return render_template('/404.html'), 404

    return app
