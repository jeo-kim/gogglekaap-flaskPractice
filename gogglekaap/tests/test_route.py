import sys # gogglekaap에 있는 것을 가져올 때에는 이렇게 경로 처리.
sys.path.append('.')


from gogglekaap.configs import TestingConfig
from gogglekaap import create_app
import pytest

@pytest.fixture
def client():
    app = create_app(TestingConfig())

    with app.test_client() as client:
        yield client

def test_auth(client):
    r = client.get(
        '/auth/register',
        follow_redirects=True
    )
    assert r.status_code == 200

    r = client.get(
        '/auth/login',
        follow_redirects=True
    )
    assert r.status_code == 200

    r = client.get(
        '/auth',
        follow_redirects=True
    )
    assert r.status_code == 200

    r = client.get(
        '/auth/logout',
        follow_redirects=True
    )
    assert r.status_code == 200

def test_base(client):
    r = client.get(
        '/',
        follow_redirects = True
    )
    assert r.status_code == 200
