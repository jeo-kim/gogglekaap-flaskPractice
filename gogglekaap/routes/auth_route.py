from flask import Blueprint, render_template, redirect, url_for, flash, session, request

from gogglekaap.forms.auth_form import LoginForm, RegisterForm

NAME = 'auth'
bp = Blueprint(NAME, __name__, url_prefix='/auth')

""" only for testing """
from dataclasses import dataclass
USERS = []

@dataclass
class User:
    user_id: str
    user_name: str
    password: str

USERS.append(User('jeojeo', 'jeojeo', '1234'))
USERS.append(User('admin', 'admin', '1234'))
USERS.append(User('tester', 'tester', '1234'))



@bp.route('/')
def index():
    return redirect(url_for(f'{NAME}.login'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # POST method & validate OK
    if form.validate_on_submit():
        # 1) 유저 조회
        # 2) 존재하는 유저인지 체크
        # 3) 패스워드 정합확인
        # 4) 로그인 유지(세션)
        user_id = form.data.get('user_id')
        password = form.data.get('password')
        user = [user for user in USERS if user.user_id == user_id]
        if user:
            user = user[0]
            if user.password != password:
                flash('Password is not valid.')
            else:
                session['user_id'] = user_id
                return redirect(url_for('base.index'))
        else:
            flash(f'User_id {user_id} does not exist.')
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
        user = [user for user in USERS if user.user_id == user_id]
        if user:
            flash('User_id already exists.')
            return redirect(request.path)
        else:
            USERS.append(
                User(
                    user_id=user_id,
                    user_name=user_name,
                    password=password
                )
            )
            session['user_id'] = user_id
            return redirect(url_for('base.index'))

        return f'{user_id}, {user_name}, {password}, {repassword}'
    else:
        flash_form_errors(form)
    return render_template(f'{NAME}/register.html', form=form)


@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for(f'{NAME}.login'))

def flash_form_errors(form):
    for _, errors in form.errors.items():
        for e in errors:
            flash(e)

