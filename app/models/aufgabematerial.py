from app.extensions import db

class Aufgabematerial(db.Model):
    __tablename__ = "Aufgabematerial"

    aufgabeid = db.Column(db.Integer, primary_key=True, nullable=False)
    materialid = db.Column(db.Integer, primary_key=True, nullable=False)
    anzahl = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<Aufgabematerial {self.title}>'

    # Hilfsfunktion zur Konvertierung des Modells in ein Dictionary
    def to_dict(self):
        return {
            'aufgabeid': self.aufgabeid,
            'materialid': self.materialid,
            'anzahl': self.anzahl
        }