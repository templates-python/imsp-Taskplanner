from flask import request
from flask import jsonify
from flask import render_template

from app.aufgabe import bp
from app.models import Aufgabe
from app.extensions import db


# Index and display all Aufgaben
@bp.route('/')
def index():
    aufgaben = Aufgabe.query.all()
    return render_template('aufgabe/aufgabe.html', aufgaben=aufgaben)

# GET ohne ID (alle Aufgaben abrufen)
@bp.route('/', methods=['GET'])
def get_aufgaben():
    aufgaben = Aufgabe.query.all()
    return jsonify([aufgabe.to_dict() for aufgabe in aufgaben])

# GET mit ID (eine spezifische Aufgabe abrufen)
@bp.route('/<int:id>', methods=['GET'])
def get_aufgabe(id):
    aufgabe = Aufgabe.query.get_or_404(id)
    return jsonify(aufgabe.to_dict())

# POST (eine neue Aufgabe erstellen)
@bp.route('/', methods=['POST'])
def create_aufgabe():
    data = request.get_json() or {}

    aufgabe = Aufgabe(
        seriemasterid=data.get('seriemasterid',None),
        titel=data.get('titel'),
        beginn=data.get('beginn'),
        ende=data.get('ende'),
        ort=data.get('ort', ''),
        koordinaten=data.get('koordinaten', ''),
        notiz=data.get('notiz', ''),
        kategorieid=data.get('kategorieid'),
        prioritaetid=data.get('prioritaetid'),
        fortschrittid=data.get('fortschrittid')
    )
    db.session.add(aufgabe)
    db.session.commit()
    return jsonify(aufgabe.to_dict()), 201

# PUT (eine existierende Aufgabe aktualisieren)
@bp.route('/<int:id>', methods=['PUT'])
def update_aufgabe(id):
    aufgabe = Aufgabe.query.get_or_404(id)
    data = request.get_json() or {}
    if 'seriemasterid' in data: aufgabe.seriemasterid = data['seriemasterid']
    if 'titel' in data: aufgabe.titel = data['titel']
    if 'beginn' in data: aufgabe.beginn = data['beginn']
    if 'ende' in data: aufgabe.ende = data['ende']
    if 'ort' in data: aufgabe.ort = data['ort']
    if 'koordinaten' in data: aufgabe.koordinaten = data['koordinaten']
    if 'notiz' in data: aufgabe.notiz = data['notiz']
    if 'kategorieid' in data: aufgabe.kategorieid = data['kategorieid']
    if 'prioritaetid' in data: aufgabe.prioritaetid = data['prioritaetid']
    if 'fortschrittid' in data: aufgabe.fortschrittid = data['fortschrittid']
    db.session.commit()
    return jsonify(aufgabe.to_dict())

# DELETE (eine Aufgabe löschen)
@bp.route('/<int:id>', methods=['DELETE'])
def delete_aufgabe(id):
    aufgabe = Aufgabe.query.get_or_404(id)
    db.session.delete(aufgabe)
    db.session.commit()
    return '', 204

@bp.route('/uv')
def undefined_variable():
    # This will raise a NameError because 'undefined_var' is not defined
    raise Exception("Intentional 500 error for testing purposes.")

