from app.extensions import db

class Aufgabe(db.Model):
    __tablename__ = "Aufgabe"

    aufgabeid = db.Column(db.Integer, primary_key=True)
    seriemasterid = db.Column(db.Integer, nullable=True)
    titel = db.Column(db.String(100), nullable=False)
    beginn = db.Column(db.DateTime, nullable=False)
    ende = db.Column(db.DateTime, nullable=True)
    ort = db.Column(db.String(250), nullable=True)
    koordinaten = db.Column(db.String(100), nullable=True)
    notiz = db.Column(db.Text, nullable=True)
    kategorieid = db.Column(db.Integer, db.ForeignKey('kategorie.kategorieid'), nullable=False)
    prioritaetid = db.Column(db.Integer, db.ForeignKey('prioritaet.prioritaetid'), nullable=False)
    fortschrittid = db.Column(db.Integer, db.ForeignKey('fortschritt.fortschrittid'), nullable=False)

    def __repr__(self):
        return f'<Aufgabe {self.title}>'

    # Add the to_dict method inside the class
    def to_dict(self):
        return {
            'aufgabeid': self.aufgabeid,
            'seriemasterid': self.seriemasterid,
            'titel': self.titel,
            'beginn': self.beginn,
            'ende': self.ende,
            'ort': self.ort,
            'koordinaten': self.koordinaten,
            'notiz': self.notiz,
            'kategorieid': self.kategorieid,
            'prioritaetid': self.prioritaetid,
            'fortschrittid': self.fortschrittid
        }