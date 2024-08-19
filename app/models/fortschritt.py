from app.extensions import db

class Fortschritt(db.Model):
    __tablename__ = "Fortschritt"

    fortschrittid = db.Column(db.Integer, primary_key=True)
    fortschritt = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return f'<Fortschritt {self.title}>'

    # Hilfsfunktion zur Konvertierung des Modells in ein Dictionary
    def to_dict(self):
        return {
            'fortschrittid': self.fortschrittid,
            'fortschritt': self.fortschritt
        }

