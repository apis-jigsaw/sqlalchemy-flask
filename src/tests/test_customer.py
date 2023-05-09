from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, delete
import pytest
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from tests.test_utils import get_app_with_db, delete_records
from app.models import Order, Bartender, Drink, Customer

@pytest.fixture
def build_db():
    db, app = get_app_with_db()
    with app.app_context():
        delete_records(db)

        bart = Customer(name = 'bart', hometown = "springfield", birthyear = 1970)
        db.session.add(bart)

        for i in range(2):
            order = Order()
            order.customer = bart
            db.session.add(order)
            db.session.commit()
        yield db
        delete_records(db)

def test_customer_has_many_orders(build_db):    
    first_customer = build_db.session.query(Customer).first()
    assert len(first_customer.orders) == 2

def test_customer_has_many_drinks():
    bart = Customer(name = 'bart', hometown = "springfield", birthyear = 1970)
    egg_cream = Drink(name = 'egg cream soda', calories = 80, price = 3, alcoholic = 0)
    milkshake = Drink(name = 'milkshake', calories = 300, price = 5, alcoholic = 0)
    drinks = [egg_cream, milkshake]
    db, app = get_app_with_db()
    with app.app_context():
        db.session.add(bart)
        db.session.commit()

        for i in range(2):
            order = Order()
            order.customer = bart
            order.drink = drinks[i]
            db.session.add(order)
            db.session.commit()
        
        assert len(bart.drinks) == 2