from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    # client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # assert

    assert response.json() == {'message': 'Olá Mundo!'}  # assert


def test_read_html_deve_retornar_ok_e_ola_mundo_em_html(client):
    # client = TestClient(app)  # Arrage (organização)

    response = client.get('/html')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Assert)

    assert (
        response.text
        == """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
    )


def test_create_user(client):
    # client = TestClient(app)

    response = client.post(
        '/users/',
        json={
            'username': 'hsdanield',
            'email': 'hsdanield@gmail.com',
            'password': 'supersecret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'hsdanield',
        'email': 'hsdanield@gmail.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'username': 'hsdanield', 'email': 'hsdanield@gmail.com', 'id': 1}
        ]
    }


def test_read_user_by_id(client):
    response_ok = client.get('/users/1')
    assert response_ok.status_code == HTTPStatus.OK
    assert response_ok.json() == {
        'username': 'hsdanield',
        'email': 'hsdanield@gmail.com',
        'id': 1,
    }

    response_error = client.get('/users/2')
    assert response_error.status_code == HTTPStatus.NOT_FOUND
    assert response_error.json() == {'detail': 'User not found'}


def test_update_user(client):
    response_ok = client.put(
        '/users/1',
        json={
            'username': 'hsdanield2',
            'password': 'supersecret2',
            'email': 'hsdanield@outlook.com',
        },
    )

    assert response_ok.status_code == HTTPStatus.OK
    assert response_ok.json() == {
        'username': 'hsdanield2',
        'email': 'hsdanield@outlook.com',
        'id': 1,
    }

    response_error = client.put(
        '/users/2',
        json={
            'username': 'hsdanield2',
            'password': 'supersecret2',
            'email': 'hsdanield@outlook.com',
        },
    )
    assert response_error.status_code == HTTPStatus.NOT_FOUND
    assert response_error.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response_ok = client.delete('/users/1')
    assert response_ok.status_code == HTTPStatus.OK
    assert response_ok.json() == {'message': 'User deleted successfully'}

    response_error = client.delete('/users/2')
    assert response_error.status_code == HTTPStatus.NOT_FOUND
    assert response_error.json() == {'detail': 'User not found'}
