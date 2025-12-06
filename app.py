from flask import Flask, render_template, request, redirect, flash, url_for
import os

app = Flask(__name__)
# Secret key for flash messages
app.secret_key = os.environ.get("FLASK_SECRET", "change_this_secret")

# Homepage
@app.route("/")
def home():
    return render_template("index.html", company="CENTRAL BAT")

# Contact form submission
@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    if not (name and email and message):
        flash("Merci de remplir tous les champs.", "error")
        return redirect(url_for("home") + "#contact")

    # Save message to a file
    try:
        with open("contacts.txt", "a", encoding="utf-8") as f:
            f.write(f"Nom: {name}\nEmail: {email}\nMessage: {message}\n---\n")
        flash("Merci ! Votre message a bien été envoyé.", "success")
    except Exception as e:
        flash("Une erreur est survenue lors de l'enregistrement du message.", "error")
        print("Error writing to contacts.txt:", e)

    return redirect(url_for("home") + "#contact")

if __name__ == "__main__":
    # Debug mode for local testing
    app.run(debug=True)
