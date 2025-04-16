from flask import Flask
from connection.db import db
from repository.repository import Repository
from enums import Category

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # ou postgres se estiver rodando no docker
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()  # cria as tabelas

    resultado = Repository.set_question(
        "Qual é a saída de print(2 * '3') em Python?",
        Category.PYTHON
    )

    print(resultado)