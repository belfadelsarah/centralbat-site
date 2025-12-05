from flask import Flask, render_template, request, redirect, flash, url_for
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "change_this_secret")

# Page d'accueil
@app.route("/")
def home():
    return render_template("index.html", company="CENTRAL BAT")

# Formulaire de contact
@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    if not (name and email and message):
        flash("Merci de remplir tous les champs.", "error")
        return redirect(url_for("home") + "#contact")

    # Enregistrer le message dans un fichier (exemple simple)
    with open("contacts.txt", "a", encoding="utf-8") as f:
        f.write(f"Nom: {name}\nEmail: {email}\nMessage: {message}\n---\n")

    flash("Merci ! Votre message a bien été envoyé.", "success")
    return redirect(url_for("home") + "#contact")

# Lancer le site
if __name__ == "__main__":
    app.run()
