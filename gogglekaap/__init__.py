from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

def create_app():
    print('run: create_app()')
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'asdfasdf'

    if app.config['DEBUG']:
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

    '''CSRF INIT'''
    csrf.init_app(app)

    @app.route('/')
    def index():
        app.logger.info('RUN HELLO WORLD')
        return render_template('index.html')

    from gogglekaap.forms.auth_form import LoginForm, RegisterForm
    @app.route('/auth/login', methods = ['GET', 'POST'])
    def login():
        form = LoginForm()
        # POST method & validate OK
        if form.validate_on_submit():
            # Todo
            # 1) 유저 조회
            # 2) 존재하는 유저인지 체크
            # 3) 패스워드 정합확인
            # 4) 로그인 유지(세션)
            user_id = form.data.get('user_id')
            password = form.data.get('password')
            return f'{user_id}, {password}'
        else:
            # Todo :error
            pass
        return render_template('login.html', form=form)

    @app.route('/auth/register',  methods = ['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            # Todo
            # 1) 유저 조회
            # 2) 유저 이미 존재하는지 체크
            # 3) 없으면 유저 생성
            # 4) 로그인 유지(세션)
            user_id = form.data.get('user_id')
            user_name = form.data.get('user_name')
            password = form.data.get('password')
            repassword = form.data.get('repassword')
            return f'{user_id}, {user_name}, {password}, {repassword}'
        else:
            # Todo :error
            pass
        return render_template('register.html', form=form)

    @app.route('/auth/logout')
    def logout():
        return 'logout'

    @app.errorhandler(404)
    def page_404(error):
        return render_template('/404.html'), 404

    return app
