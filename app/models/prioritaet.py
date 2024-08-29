from app.extensions import db

class Prioritaet(db.Model):
    __tablename__ = "Prioritaet"

    prioritaetid = db.Column(db.Integer, primary_key=True)
    prioritaet = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return f'<Prioritaet {self.title}>'

    # Hilfsfunktion zur Konvertierung des Modells in ein Dictionary
    def to_dict(self):
        return {
            'prioritaetid': self.prioritaetid,
            'prioritaet': self.prioritaet
        }
