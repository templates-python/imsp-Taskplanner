from flask import Blueprint
from flask import request
from flask import jsonify
from flask import abort
from flask import render_template

from app.datei import bp
from app.models import Datei
from app.extensions import db

# Index
@bp.route('/')
def index():
    return render_template('datei/datei.html')

# GET ohne ID (alle Datein abrufen)
@bp.route('/', methods=['GET'])
def get_datein():
    datein = Datei.query.all()
    return jsonify([datei.to_dict() for datei in datein])

# GET mit ID (eine spezifische Datei abrufen)
@bp.route('/<int:id>', methods=['GET'])
def get_datei(id):
    datei = Datei.query.get_or_404(id)
    return jsonify(datei.to_dict())

# POST (eine neue Datei erstellen)
@bp.route('/', methods=['POST'])
def create_datei():
    data = request.get_json() or {}
    datei = Datei(
        dateipfad=data.get('dateipfad'),
        dateiblob=data.get('dateiblob'),
        aufgabeid=data.get('aufgabeid')
    )
    db.session.add(datei)
    db.session.commit()
    return jsonify(datei.to_dict()), 201

# PUT (eine existierende Datei aktualisieren)
@bp.route('/<int:id>', methods=['PUT'])
def update_datei(id):
    datei = Datei.query.get_or_404(id)
    data = request.get_json() or {}
    if 'dateipfad' in data: datei.dateipfad = data['dateipfad']
    if 'dateiblob' in data: datei.dateiblob = data['dateiblob']
    if 'aufgabeid' in data: datei.aufgabeid = data['aufgabeid']
    db.session.commit()
    return jsonify(datei.to_dict())

# DELETE (eine Datei löschen)
@bp.route('/<int:id>', methods=['DELETE'])
def delete_datei(id):
    datei = Datei.query.get_or_404(id)
    db.session.delete(datei)
    db.session.commit()
    return '', 204
