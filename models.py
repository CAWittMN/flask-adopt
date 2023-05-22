from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://img.freepik.com/premium-vector/set-black-silhouettes-pets-isolated-icons-dogs-cats-rabbit-parrot_647716-78.jpg?w=826"


class Pet(db.Model):
    """Pet model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default=DEFAULT_IMAGE_URL)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    @property
    def return_image_url(self):
        """Return pet photo url"""
        if self.photo_url == DEFAULT_IMAGE_URL:
            return ""
        return self.photo_url


def connect_db(app):
    db.init_app(app)
