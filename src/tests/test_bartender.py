from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, delete
import pytest
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from tests.test_utils import get_app_with_db, delete_records
from app.models import Order, Bartender, Drink

@pytest.fixture
def build_db():
    db, app = get_app_with_db()
    with app.app_context():
        delete_records(db)

        bartender = Bartender(name = 'moe', hometown = "springfield", birthyear = 1970)
        db.session.add(bartender)

        for i in range(2):
            order = Order()
            order.bartender = bartender
            db.session.add(order)
            db.session.commit()
        yield db
        delete_records(db)

def test_bartender_has_many_orders(build_db):    
    first_bartender = build_db.session.query(Bartender).first()
    assert len(first_bartender.orders) == 2

def test_bartender_has_many_drinks():
    bartender = Bartender(name = 'moe', hometown = "springfield", birthyear = 1970)
    egg_cream = Drink(name = 'egg cream soda', calories = 80, price = 3, alcoholic = 0)
    milkshake = Drink(name = 'milkshake', calories = 300, price = 5, alcoholic = 0)
    drinks = [egg_cream, milkshake]
    db, app = get_app_with_db()
    with app.app_context():
        db.session.add(bartender)
        db.session.commit()

        for i in range(2):
            order = Order()
            order.bartender = bartender
            order.drink = drinks[i]
            db.session.add(order)
            db.session.commit()
        
        assert len(bartender.drinks) == 2