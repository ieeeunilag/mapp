# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from mapp import db

from mapp.libs.database import Base

class Radiography(Base):
    """
    Schema for radiography table
    """
    __tablename__ = "radiography"

    sur_name = db.Column(db.String(100), nullable=False)
    other_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    age = db.Column(db.Integer, nullable=False)
