from flask import Blueprint
from flask import request
from flask import jsonify
from flask import abort
from flask import render_template

from app.prioritaet import bp
from app.models import Prioritaet
from app.extensions import db

# Index
@bp.route('/')
def index():
    return render_template('prioritaet/prioritaet.html')

# GET ohne ID (alle Prioritaetn abrufen)
@bp.route('/', methods=['GET'])
def get_prioritaetn():
    prioritaetn = Prioritaet.query.all()
    return jsonify([prioritaet.to_dict() for prioritaet in prioritaetn])

# GET mit ID (eine spezifische Prioritaet abrufen)
@bp.route('/<int:id>', methods=['GET'])
def get_prioritaet(id):
    prioritaet = Prioritaet.query.get_or_404(id)
    return jsonify(prioritaet.to_dict())

# POST (eine neue Prioritaet erstellen)
@bp.route('/', methods=['POST'])
def create_prioritaet():
    data = request.get_json() or {}

    prioritaet = Prioritaet(
        prioritaet=data.get('prioritaet')
    )
    db.session.add(prioritaet)
    db.session.commit()
    return jsonify(prioritaet.to_dict()), 201

# PUT (eine existierende Prioritaet aktualisieren)
@bp.route('/<int:id>', methods=['PUT'])
def update_prioritaet(id):
    prioritaet = Prioritaet.query.get_or_404(id)
    data = request.get_json() or {}
    if 'prioritaet' in data: prioritaet.prioritaet = data['prioritaet']
    db.session.commit()
    return jsonify(prioritaet.to_dict())

# DELETE (eine Prioritaet löschen)
@bp.route('/<int:id>', methods=['DELETE'])
def delete_prioritaet(id):
    prioritaet = Prioritaet.query.get_or_404(id)
    db.session.delete(prioritaet)
    db.session.commit()
    return '', 204

