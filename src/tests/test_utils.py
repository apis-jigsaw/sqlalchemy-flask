from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.models import Order, Bartender, Drink, Customer

def get_app_with_db():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    TEST_URL = 'postgresql://localhost/moes_bar_test'
    app.config['SQLALCHEMY_DATABASE_URI'] = TEST_URL
    db = SQLAlchemy()
    db.init_app(app)
    return db, app

def delete_records(db):
    db.session.query(Order).delete()
    db.session.query(Bartender).delete()
    db.session.query(Drink).delete()
    db.session.query(Customer).delete()