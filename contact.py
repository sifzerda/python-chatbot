from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Create a Blueprint for contact-related routes
contact_bp = Blueprint("contact", __name__, template_folder="templates")

# Database initialization (import this from your main app file)
db = SQLAlchemy()

# Define the Message model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Routes for the Contact Blueprint
@contact_bp.route("/contact")
def contact():
    # Retrieve all messages from the database, ordered by the most recent first
    messages = Message.query.order_by(Message.id.desc()).all()
    return render_template("contact.html", messages=messages)

@contact_bp.route("/contact/submit", methods=["POST"])
def submit():
    try:
        name = request.form["name"]
        message = request.form["message"]
        if not name or not message:
            flash("All fields are required!", "error")
            return redirect(url_for("contact.contact"))

        # Save the message to the database
        new_message = Message(name=name, message=message)
        db.session.add(new_message)
        db.session.commit()

        flash("Message sent successfully!", "success")
        return redirect(url_for("contact.contact"))
    except Exception as e:
        flash(f"An error occurred: {e}", "error")
        return redirect(url_for("contact.contact"))

@contact_bp.route("/messages")
def view_messages():
    messages = Message.query.order_by(Message.id.desc()).all()
    return render_template("messages.html", messages=messages)