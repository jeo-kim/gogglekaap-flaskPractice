from flask import Blueprint, render_template, redirect, url_for, flash

from gogglekaap.forms.auth_form import LoginForm, RegisterForm

NAME = 'auth'
bp = Blueprint(NAME, __name__, url_prefix='/auth')

@bp.route('/')
def index():
    return redirect(url_for(f'{NAME}.login'))

@bp.route('/login', methods=['GET', 'POST'])
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
        flash_form_errors(form)
    return render_template(f'{NAME}/login.html', form=form)


@bp.route('/register', methods=['GET', 'POST'])
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
        flash_form_errors(form)
    return render_template(f'{NAME}/register.html', form=form)


@bp.route('/logout')
def logout():
    return 'logout'

def flash_form_errors(form):
    for _, errors in form.errors.items():
        for e in errors:
            flash(e)

