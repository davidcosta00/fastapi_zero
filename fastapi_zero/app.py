from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


@app.get('/exercicio/2', response_class=HTMLResponse)
def exercicio_segunda_aula():
    return """
    <html>
        <body>
            <div>Olá Mundo!</div>
        </body>
    </html>"""
