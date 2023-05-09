from sqlalchemy.orm import relationship, backref
from app import db

class Bartender(db.Model):
    __tablename__ = 'bartenders'

    id = db.Column(db.Integer, primary_key=True, server_default="nextval('my_table_id_seq')")
    name = db.Column(db.String(80), unique=True, nullable=False)
    hometown = db.Column(db.String(120), unique=True, nullable=False)
    birthyear = db.Column(db.Integer(), unique=True, nullable=False)

    # orders = relationship('Order', backref=backref('bartender'), cascade='all, delete-orphan')
    orders = relationship('Order', back_populates = 'bartender', cascade='all, delete-orphan')

    drinks = db.relationship('Drink', secondary='orders', overlaps="bartender,orders")
    


    def to_dict(self):
        dict_ = {}
        for key in self.__mapper__.c.keys():
            dict_[key] = getattr(self, key)
        return dict_


    def __repr__(self):
        return '<Bartender %r>' % self.name