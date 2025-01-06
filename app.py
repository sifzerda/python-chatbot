from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from contact import contact_bp, db

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flash messages

# Configure the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///messages.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Register the contact blueprint
app.register_blueprint(contact_bp)

# Main routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/chatbot")
def bot():
    return render_template("chatbot.html")

# Run the application
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)