from app.extensions import db

class Kategorie(db.Model):
    __tablename__ = "Kategorie"

    kategorieid = db.Column(db.Integer, primary_key=True)
    kategorie = db.Column(db.String(100), nullable=False)
    istaktiv = db.Column(db.Boolean, nullable=True, default=True)


    def __repr__(self):
        return f'<Kategorie {self.title}>'

    # Hilfsfunktion zur Konvertierung des Modells in ein Dictionary
    def to_dict(self):
        return {
            'kategorieid': self.kategorieid,
            'kategorie': self.kategorie,
            'istaktiv': self.istaktiv
        }