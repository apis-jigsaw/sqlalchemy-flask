from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, delete
import pytest
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from tests.test_utils import get_app_with_db, delete_records
from app.models import Order, Bartender, Drink


@pytest.fixture
def db():
    db, app = get_app_with_db()
    with app.app_context():
        delete_records(db)
        for i in range(2):
            order = Order()
            bartender = Bartender(name = 'moe', hometown = "springfield", birthyear = 1970)
            db.session.add(bartender)
            order.bartender = bartender
            db.session.add(order)
            db.session.commit()
        yield db

        delete_records(db)
        
def test_order_has_associated_bartender(db):
    first_order = db.session.query(Order).first()
    assert first_order.bartender.name == 'moe'

def test_order_has_associated_drink():
    db, app = get_app_with_db()
    with app.app_context():
        delete_records(db)
        milkshake = Drink(name = 'milkshake', calories = 300, price = 5, alcoholic = 0)
        db.session.add(milkshake)
        order = Order()
        order.drink = milkshake
        db.session.add(order)
        db.session.commit()
        first_order = db.session.query(Order).first()
        assert first_order.drink.name == 'milkshake'



