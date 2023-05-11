from imdb_data import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    imdb_id = db.Column(db.String(10), nullable=False)
