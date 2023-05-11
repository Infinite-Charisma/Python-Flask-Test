from flask import Blueprint, render_template, request

from imdb_data.main.services import store_movies
from imdb_data.models import Movie

main = Blueprint('main',__name__ )

@main.route("/store_movie",methods = ['GET','POST'])
def cli_retrieve_movies():
    if request.method == "POST":
        message = store_movies()
        return render_template("store_movie.html", message=message)
    return render_template("store_movie.html")



@main.route("/movies",methods = ['GET'])
def index():
    # Retrieve the movies from the database
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)
