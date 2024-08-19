from app.extensions import db

class Datei(db.Model):
    __tablename__ = "Datei"

    dateiid = db.Column(db.Integer, primary_key=True)
    dateipfad = db.Column(db.String(250), nullable=False)
    dateiblob = db.Column(db.LargeBinary, nullable=True)
    aufgabeid = db.Column(db.Integer, db.ForeignKey('aufgabe.aufgabeid'), nullable=False)

    def __repr__(self):
        return f'<Datei {self.title}>'

    # Hilfsfunktion zur Konvertierung des Modells in ein Dictionary
    def to_dict(self):
        return {
            'dateipfad': self.dateipfad,
            'dateiblob': self.dateiblob,
            'aufgabeid': self.aufgabeid
        }

