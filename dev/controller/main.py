from flask import Blueprint, render_template

# Blueprint für Index definieren
main = Blueprint('main', __name__)

# Standard-Route für Root-Pfad
@main.route('/')
def index():
    # Rendert die Template-Datei templates/index.html
    return render_template('index.html')    