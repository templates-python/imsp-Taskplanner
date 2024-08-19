from flask import Blueprint
from flask import request
from flask import jsonify
from flask import abort
from flask import render_template

from app.kategorie import bp
from app.models import Kategorie
from app.extensions import db

# Index
@bp.route('/')
def index():
    return render_template('kategorie/kategorie.html')

# GET ohne ID (alle Kategorien abrufen)
@bp.route('/', methods=['GET'])
def get_kategorien():
    kategorien = Kategorie.query.all()
    return jsonify([kategorie.to_dict() for kategorie in kategorien])

# GET mit ID (eine spezifische Kategorie abrufen)
@bp.route('/<int:id>', methods=['GET'])
def get_kategorie(id):
    kategorie = Kategorie.query.get_or_404(id)
    return jsonify(kategorie.to_dict())

# POST (eine neue Kategorie erstellen)
@bp.route('/', methods=['POST'])
def create_kategorie():
    data = request.get_json() or {}

    kategorie = Kategorie(
        kategorie=data.get('kategorie'),
        istaktiv = data.get('istaktiv')
    )
    db.session.add(kategorie)
    db.session.commit()
    return jsonify(kategorie.to_dict()), 201

# PUT (eine existierende Kategorie aktualisieren)
@bp.route('/<int:id>', methods=['PUT'])
def update_kategorie(id):
    kategorie = Kategorie.query.get_or_404(id)
    data = request.get_json() or {}
    if 'kategorie' in data: kategorie.kategorie = data['kategorie']
    if 'istaktiv' in data: kategorie.istaktiv = data['istaktiv']
    db.session.commit()
    return jsonify(kategorie.to_dict())

# DELETE (eine Kategorie löschen)
@bp.route('/<int:id>', methods=['DELETE'])
def delete_kategorie(id):
    kategorie = Kategorie.query.get_or_404(id)
    db.session.delete(kategorie)
    db.session.commit()
    return '', 204

