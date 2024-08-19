from flask import Flask
from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.aufgabe import bp as aufgabe_bp
    app.register_blueprint(aufgabe_bp, url_prefix='/aufgabe')

    from app.aufgabematerial import bp as aufgabematerial_bp
    app.register_blueprint(aufgabematerial_bp, url_prefix='/aufgabematerial')

    from app.datei import bp as datei_bp
    app.register_blueprint(datei_bp, url_prefix='/datei')

    from app.fortschritt import bp as fortschritt_bp
    app.register_blueprint(fortschritt_bp, url_prefix='/fortschritt')

    from app.kategorie import bp as kategorie_bp
    app.register_blueprint(kategorie_bp, url_prefix='/kategorie')

    from app.material import bp as material_bp
    app.register_blueprint(material_bp, url_prefix='/material')

    from app.prioritaet import bp as prioritaet_bp
    app.register_blueprint(prioritaet_bp, url_prefix='/prioritaet')

    return app