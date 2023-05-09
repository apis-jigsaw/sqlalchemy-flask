from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    conn_str = "postgresql://localhost:5432/moes_bar"
    app.config['SQLALCHEMY_DATABASE_URI'] = conn_str
    db.init_app(app)
    return app
    