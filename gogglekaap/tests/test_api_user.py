def test_get_users(client):
    r = client.get(
        'api/users',
        follow_redirects=True
    )
    assert r.status_code == 200
    print(r.json)
    assert len(r.json) == 1

def test_get_user(client, user_data):
    r = client.get(
        '/api/users/1',
        follow_redirects=True
    )
    assert r.status_code == 200
    assert r.json.get('user_id') == user_data.get('user_id')

def test_post_user(client, user_data):
    r = client.post(
        '/api/users',
        data=user_data
    )
    # 왜 400으로 나오지? # production 모드여서 그랬구나, csrf 토큰이 안 들어가져서..! -> dev모드로 다시.
    assert r.status_code == 409
    new_user_data = user_data.copy()
    new_user_data['user_id'] = 'tester2'
    r = client.post(
        '/api/users',
        data=new_user_data
    )
    assert r.status_code == 201