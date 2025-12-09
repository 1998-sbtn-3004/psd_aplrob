from flask import Flask
from config import get_config

# Blueprints aus dem controller Ordner importieren
from controller.main import main

# -------------------------------------------------------
# Funktion zum einstellen und starten der App
# -------------------------------------------------------
def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    # -------------------------------------------------------
    # ToDo: Erweiterungen initialisieren
    # -------------------------------------------------------
    
    # -------------------------------------------------------
    # Blueprints registrieren
    # -------------------------------------------------------
    app.register_blueprint(main)    
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)