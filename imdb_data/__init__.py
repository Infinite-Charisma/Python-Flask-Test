from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from imdb_data.config import Config

load_dotenv()


db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    print(Config.SQLALCHEMY_DATABASE_URI)
    db.init_app(app)

    from imdb_data.main.routes import main
    app.register_blueprint(main)

    return  app
