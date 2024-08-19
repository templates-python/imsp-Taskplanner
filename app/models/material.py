from app.extensions import db

class Material(db.Model):
    __tablename__ = "Material"

    materialid = db.Column(db.Integer, primary_key=True)
    material = db.Column(db.String(100), nullable=False)
    istaktiv = db.Column(db.Boolean, nullable=True, default=True)


    def __repr__(self):
        return f'<Material {self.title}>'

    # Hilfsfunktion zur Konvertierung des Modells in ein Dictionary
    def  to_dict(self):
        return {
            'materialid': self.materialid,
            'material': self.material,
            'istaktiv': self.istaktiv
        }
