from sqlalchemy.orm import relationship, backref
from app import db

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True, server_default="nextval('my_table_id_seq')")
    name = db.Column(db.String(80), unique=True, nullable=False)
    hometown = db.Column(db.String(120), unique=True, nullable=False)
    birthyear = db.Column(db.Integer(), unique=True, nullable=False)

    orders = relationship('Order', back_populates = 'customer', cascade='all, delete-orphan')
    
    drinks = db.relationship('Drink', secondary='orders', overlaps="bartender,orders")

    