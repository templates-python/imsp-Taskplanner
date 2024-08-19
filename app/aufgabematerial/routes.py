from flask import Blueprint
from flask import request
from flask import jsonify
from flask import abort
from flask import render_template

from app.aufgabematerial import bp
from app.models import Aufgabematerial
from app.extensions import db

# Index
@bp.route('/')
def index():
    return render_template('aufgabematerial/aufgabematerial.html')

# GET ohne ID (alle aufgabematerialn abrufen)
@bp.route('/', methods=['GET'])
def get_aufgabematerialien():
    aufgabematerialien = Aufgabematerial.query.all()
    return jsonify([aufgabematerial.to_dict() for aufgabematerial in aufgabematerialien])

# GET mit ID (eine spezifische aufgabematerial abrufen)
@bp.route('/<int:id>', methods=['GET'])
def get_aufgabematerial(id):
    aufgabematerial = Aufgabematerial.query.get_or_404(id)
    return jsonify(aufgabematerial.to_dict())

# POST (eine neue aufgabematerial erstellen)
@bp.route('/', methods=['POST'])
def create_aufgabematerial():
    data = request.get_json() or {}
    aufgabematerial = Aufgabematerial(
        aufgabeid=data.get('aufgabeid'),
        materialid=data.get('aterialid'),
        anzahl=data.get('anzahl',1),
    )
    db.session.add(aufgabematerial)
    db.session.commit()
    return jsonify(aufgabematerial.to_dict()), 201

# PUT (eine existierende aufgabematerial aktualisieren)
@bp.route('/<int:id>', methods=['PUT'])
def update_aufgabematerial(id):
    aufgabematerial = Aufgabematerial.query.get_or_404(id)
    data = request.get_json() or {}
    if 'aufgabeid' in data: aufgabematerial.aufgabeid = data['aufgabeid']
    if 'materialid' in data: aufgabematerial.materialid = data['materialid']
    if 'anzahl' in data: aufgabematerial.anzahl = data['anzahl']
    db.session.commit()
    return jsonify(aufgabematerial.to_dict())

# DELETE (eine aufgabematerial löschen)
@bp.route('/<int:id>', methods=['DELETE'])
def delete_aufgabematerial(id):
    aufgabematerial = Aufgabematerial.query.get_or_404(id)
    db.session.delete(aufgabematerial)
    db.session.commit()
    return '', 204

