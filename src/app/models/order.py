from app import db
from sqlalchemy.orm import relationship, backref
class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    bartender_id = db.Column(db.Integer(), db.ForeignKey('bartenders.id'))
    drink_id = db.Column(db.Integer(), db.ForeignKey('drinks.id'))
    customer_id = db.Column(db.Integer(), db.ForeignKey('customers.id'))
    drink = relationship('Drink', back_populates='orders', overlaps="bartenders,drinks")
    
    customer = relationship('Customer', back_populates = 'orders')
    bartender = relationship('Bartender', back_populates = 'orders')

    def __repr__(self):
        return f'<Order id: {self.id}, customer_id: {self.customer_id}, drink_id: {self.drink_id}, bartender_id: {self.bartender_id}>'
