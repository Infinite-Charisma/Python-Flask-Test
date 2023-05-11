import requests
from imdb_data import db
from imdb_data.models import Movie

def store_movies():
    try:
        query = """
            SELECT ?movie ?movieLabel ?imdbId WHERE {
              ?movie wdt:P31 wd:Q11424.
              ?movie wdt:P577 ?date.
              ?movie wdt:P345 ?imdbId.
              FILTER(year(?date) > 2013).
              SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
            }
            """
        url = "https://query.wikidata.org/sparql"
        params = {"query": query, "format": "json"}
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(url, params=params, headers=headers)
        print(response.content)
        movies = response.json()["results"]["bindings"]
        for movie in movies:
            name = movie["movieLabel"]["value"]
            imdb_id = movie["imdbId"]["value"].split("/")[-1]
            movie = Movie(name=name, imdb_id=imdb_id)
            db.session.add(movie)

        db.session.commit()
        message = "Succesfully Stored Data"
    except Exception as e:
        message = f"Error: {str(e)}"
    return message
