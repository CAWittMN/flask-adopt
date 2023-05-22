from flask import Flask, render_template, redirect, flash, jsonify, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet, DEFAULT_IMAGE_URL
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "fluffyanimals"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_RECORD_QUERIES"] = True
app.debug = True

debug = DebugToolbarExtension(app)

connect_db(app)

with app.app_context():
    db.create_all()


@app.route("/")
def show_home_page():
    """Show home page and list of all pets."""

    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route("/pet/<int:pet_id>")
def show_pet_page(pet_id):
    """Show a specific pet."""

    pet = Pet.query.get_or_404(pet_id)
    return render_template("pet.html", pet=pet)


@app.route("/pet/<int:pet_id>/edit", methods=["GET", "POST"])
def edit_pet_page(pet_id):
    """Edit a specific pet."""

    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.photo_url = form.photo_url.data or DEFAULT_IMAGE_URL
        pet.available = form.available.data
        db.session.commit()
        return redirect(url_for("show_pet_page", pet_id=pet_id))

    return render_template("edit-pet.html", form=form, pet=pet)


@app.route("/pet/add", methods=["GET", "POST"])
def add_pet_page():
    """Add a new pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        pet = Pet(
            name=form.name.data,
            species=form.species.data,
            notes=form.notes.data,
            age=form.age.data,
        )

        db.session.add(pet)
        db.session.commit()
        return redirect(url_for("show_home_page"))

    return render_template("add-pet.html", form=form)


@app.route("/pet/<int:pet_id>/delete", methods=["POST"])
def delete_pet(pet_id):
    """Delete a pet."""

    pet = Pet.query.get(pet_id)

    db.session.delete(pet)
    db.session.commit()
    return redirect("/")
