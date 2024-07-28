from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # assert

    assert response.json() == {'message': 'Olá Mundo!'}  # assert


def test_read_html_deve_retornar_ok_e_ola_mundo_em_html():
    client = TestClient(app)  # Arrage (organização)

    response = client.get('/html')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Assert)

    assert response.text == """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
