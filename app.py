from flask import Flask, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)

toolbar = DebugToolbarExtension(app)

app.config["SECRET_KEY"] = "fluffyanimals"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

connect_db(app)
with app.app_context():
    db.create_all()
