from flask import Flask
from config.settings import Settings
from connection import db
from controller import bp as routes_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = Settings.get_database_uri()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(routes_bp)

    with app.app_context():
        db.create_all()  # Cria as tabelas no banco se ainda não existirem

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)