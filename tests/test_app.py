from http import HTTPStatus

from bs4 import BeautifulSoup as bs
from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)

    response = client.get('/')
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_exercicio_segunda_aula_ola_mundo():
    client = TestClient(app)

    response = client.get('/exercicio/2')
    response = bs(response, 'html.parser')
    assert response.status_code == HTTPStatus.OK
    assert response.find({'div'}).text == 'Olá Mundo!'
