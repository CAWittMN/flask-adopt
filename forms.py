from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired(), Length(min=1, max=30)])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    species = SelectField(
        "Animal kind",
        choices=[
            ("dog", "Dog"),
            ("cat", "Cat"),
            ("bird", "Bird"),
            ("reptile", "Reptile"),
            ("fish", "Fish"),
            ("rodent", "Rodent"),
        ],
        validators=[InputRequired()],
    )
    age = IntegerField("Age", validators=[InputRequired(), NumberRange(min=0, max=100)])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=0, max=1000)])


class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("comments", validators=[Optional(), Length(min=0, max=1000)])
    available = BooleanField("Adoptable?")
