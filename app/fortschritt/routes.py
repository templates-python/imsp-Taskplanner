from flask import request
from flask import jsonify
from flask import render_template

from app.fortschritt import bp
from app.models import Fortschritt
from app.extensions import db

# Index
@bp.route('/')
def index():
    return render_template('fortschritt/fortschritt.html')

# GET ohne ID (alle Fortschrittn abrufen)
@bp.route('/', methods=['GET'])
def get_fortschritte():
    fortschritte = Fortschritt.query.all()
    return jsonify([fortschritt.to_dict() for fortschritt in fortschritte])

# GET mit ID (eine spezifische Fortschritt abrufen)
@bp.route('/<int:id>', methods=['GET'])
def get_fortschritt(id):
    fortschritt = Fortschritt.query.get_or_404(id)
    return jsonify(fortschritt.to_dict())

# POST (eine neue Fortschritt erstellen)
@bp.route('/', methods=['POST'])
def create_fortschritt():
    data = request.get_json() or {}

    fortschritt = Fortschritt(
        fortschritt=data.get('fortschritt')
    )
    db.session.add(fortschritt)
    db.session.commit()
    return jsonify(fortschritt.to_dict()), 201

# PUT (eine existierende Fortschritt aktualisieren)
@bp.route('/<int:id>', methods=['PUT'])
def update_fortschritt(id):
    fortschritt = Fortschritt.query.get_or_404(id)
    data = request.get_json() or {}
    if 'fortschritt' in data: fortschritt.fortschritt = data['fortschritt']
    db.session.commit()
    return jsonify(fortschritt.to_dict())

# DELETE (eine Fortschritt löschen)
@bp.route('/<int:id>', methods=['DELETE'])
def delete_fortschritt(id):
    fortschritt = Fortschritt.query.get_or_404(id)
    db.session.delete(fortschritt)
    db.session.commit()
    return '', 204

