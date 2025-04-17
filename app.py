from flask import Flask
from config.settings import Settings
from connection.database import db
from controller.controller import TestController 


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = Settings.get_database_uri()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


with app.app_context():
    db.create_all()  # Cria as tabelas no banco se ainda não existirem

TestController(app)

if __name__ == "__main__":
    app.run(debug=True)