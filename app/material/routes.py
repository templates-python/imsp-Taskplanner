from flask import Blueprint
from flask import request
from flask import jsonify
from flask import abort
from flask import render_template

from app.material import bp
from app.models import Material
from app.extensions import db

# Index
@bp.route('/')
def index():
    return render_template('material/material.html')

# GET ohne ID (alle Materialn abrufen)
@bp.route('/', methods=['GET'])
def get_materialn():
    materialn = Material.query.all()
    return jsonify([material.to_dict() for material in materialn])

# GET mit ID (eine spezifische Material abrufen)
@bp.route('/<int:id>', methods=['GET'])
def get_material(id):
    material = Material.query.get_or_404(id)
    return jsonify(material.to_dict())

# POST (eine neue Material erstellen)
@bp.route('/', methods=['POST'])
def create_material():
    data = request.get_json() or {}

    material = Material(
        material=data.get('material'),
        istaktiv = data.get('istaktiv')
    )
    db.session.add(material)
    db.session.commit()
    return jsonify(material.to_dict()), 201

# PUT (eine existierende Material aktualisieren)
@bp.route('/<int:id>', methods=['PUT'])
def update_material(id):
    material = Material.query.get_or_404(id)
    data = request.get_json() or {}
    if 'material' in data: material.material = data['material']
    if 'istaktiv' in data: material.istaktiv = data['istaktiv']
    db.session.commit()
    return jsonify(material.to_dict())

# DELETE (eine Material löschen)
@bp.route('/<int:id>', methods=['DELETE'])
def delete_material(id):
    material = Material.query.get_or_404(id)
    db.session.delete(material)
    db.session.commit()
    return '', 204


