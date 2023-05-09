from sqlalchemy.orm import relationship, backref
from app import db

class Drink(db.Model):
    __tablename__ = 'drinks'

    id = db.Column(db.Integer, primary_key=True, server_default="nextval('my_table_id_seq')")
    name = db.Column(db.String(80), unique=True, nullable=False)

    calories = db.Column(db.Integer())
    price = db.Column(db.Integer())
    alcoholic = db.Column(db.Integer())

    orders = relationship('Order', back_populates='drink', overlaps="bartenders,drinks")
    bartenders = db.relationship('Bartender', secondary='orders', overlaps="bartender, drinks,orders")
