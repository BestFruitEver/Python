from flask import Flask, url_for,abort,redirect

app = Flask(__name__)

@app.route("/accueil")
def index():
    return 'Hello world ! <img src="' + url_for('static',filename = 'banniere.jpg') + '" alt="logo">'

@app.route("/about")
def about():
    return "Ceci est la page about"

@app.route("/profil/<string:username>")
def profil(username):
    return 'Bonjour ' + username

@app.route("/contact")
def contact():
    return 'Page contact <a href="' + url_for('index') + '">Retour accueil</a>'

@app.route('/protected/<int:code>')
def protected(code):
    if code == 1234:
        return 'Accès autorisé'
    else:
        return redirect(url_for('user_login'))

@app.route('/login')
def user_login():
    return "Merci de vous identifier"