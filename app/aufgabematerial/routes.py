from flask import request
from flask import jsonify
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
@bp.route('/aufgabe/<int:aufgabeid>/material/<int:materialid>', methods=['GET'])
def get_aufgabematerial(aufgabeid, materialid):
    aufgabematerial = Aufgabematerial.query.filter_by(aufgabeid=aufgabeid, materialid=materialid).first()
    return jsonify(aufgabematerial.to_dict())


# POST (eine neue aufgabematerial erstellen)
@bp.route('/', methods=['POST'])
def create_aufgabematerial():
    data = request.get_json() or {}
    aufgabematerial = Aufgabematerial(
        aufgabeid=data.get('aufgabeid'),
        materialid=data.get('materialid'),
        anzahl=data.get('anzahl', 1),
    )
    db.session.add(aufgabematerial)
    db.session.commit()
    return jsonify(aufgabematerial.to_dict()), 201


# PUT (eine existierende aufgabematerial aktualisieren)
@bp.route('/aufgabe/<int:aufgabeid>/material/<int:materialid>', methods=['PUT'])
def update_aufgabematerial(aufgabeid,materialid):
    aufgabematerial = Aufgabematerial.query.filter_by(aufgabeid=aufgabeid, materialid=materialid).first()
    data = request.get_json() or {}
    if 'aufgabeid' in data: aufgabematerial.aufgabeid = data['aufgabeid']
    if 'materialid' in data: aufgabematerial.materialid = data['materialid']
    if 'anzahl' in data: aufgabematerial.anzahl = data['anzahl']
    db.session.commit()
    return jsonify(aufgabematerial.to_dict())

# DELETE (eine aufgabematerial löschen)
@bp.route('/aufgabe/<int:aufgabeid>/material/<int:materialid>', methods=['DELETE'])
def delete_aufgabematerial(aufgabeid,materialid):
    aufgabematerial = Aufgabematerial.query.filter_by(aufgabeid=aufgabeid, materialid=materialid).first()
    db.session.delete(aufgabematerial)
    db.session.commit()
    return '', 204
