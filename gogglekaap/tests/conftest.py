import sys # gogglekaap에 있는 것을 가져올 때에는 이렇게 경로 처리.
sys.path.append('.')


from gogglekaap.configs import TestingConfig
from gogglekaap import create_app, db
from gogglekaap.models.user import User as UserModel
from gogglekaap.models.memo import Memo as MemoModel
import pytest
import os

@pytest.fixture(scope='session')
def user_data():
    yield dict (
        user_id='tester',
        user_name='tester',
        password='tester'
    )

@pytest.fixture(scope='session')
def memo_data():
    yield dict(
        title='title',
        content='content'
    )

@pytest.fixture(scope='session')
def app(user_data, memo_data):
    app = create_app(TestingConfig())
    with app.app_context():
        db.drop_all()
        db.create_all()
        user = UserModel(**user_data)
        db.session.add(user)
        db.session.flush()  # commit 하기 전에 아래처럼 정보를 가져오려면 flush()를 해줘야 한다.
        memo_data['user_id'] = user.id
        db.session.add(MemoModel(**memo_data))
        db.session.commit()
        yield app
        # 불필요 디비 정리
        db.drop_all()
        db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace(
            'sqlite://', ''
        )
        if os.path.isfile(db_path):
            os.remove(db_path)

@pytest.fixture(scope='session')
def client(app, user_data):
    with app.test_client() as client:
        # NOTE: 세션 입혀주기
        with client.session_transaction() as session:
            session['user_id'] = user_data.get('user_id')
        yield client
