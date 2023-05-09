from app import create_app, db
from flask import jsonify
from app.models import Bartender, Order, Customer

app = create_app()

@app.route('/bartenders')
def bartenders():
    bartenders = db.session.query(Bartender).all()
    bartender_dicts = [bartender.to_dict() for bartender in bartenders]
    
    return jsonify(bartender_dicts)

@app.route('/bartenders/<int:id>')
def bartender(id):
    bartender_dict = Bartender.query.get(id).to_dict()
    return jsonify(bartender_dict)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Bartender': Bartender, 'Order': Order, 'Customer': Customer}