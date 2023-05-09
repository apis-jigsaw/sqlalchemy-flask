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
        milkshake = Drink(name = 'milkshake', calories = 300, price = 5, alcoholic = 0)
        db.session.add(milkshake)
        db.session.commit()

        for i in range(3):
            
            order = Order()
            order.drink = milkshake
            db.session.add(order)
            db.session.commit()
        yield db
        delete_records(db)
        

def test_drink_has_many_orders(build_db):
    first_drink = build_db.session.query(Drink).first()
    assert len(first_drink.orders) == 3

def test_drink_has_many_bartenders():
    moe = Bartender(name = 'moe', hometown = "springfield", birthyear = 1970)
    sally = Bartender(name = 'sally', hometown = "springfield", birthyear = 1970)
    egg_cream = Drink(name = 'egg cream soda', calories = 80, price = 3, alcoholic = 0)
    
    bartenders = [moe, sally]
    db, app = get_app_with_db()
    with app.app_context():
        db.session.add(egg_cream)
        db.session.commit()

        for i in range(2):
            order = Order()
            order.drink = egg_cream
            order.bartender = bartenders[i]
            
            db.session.add(order)
            db.session.commit()
        
        assert len(egg_cream.bartenders) == 2