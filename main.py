from flask import Flask, jsonify
from utils import get_by_title, get_by_years, rating_children, rating_family, rating_adult, get_by_genre

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_AS_ASCII'] = False


@app.route('/movie/<title>')
def get_film_by_title(title):
    film = get_by_title(title)
    return jsonify(film)


@app.route('/<int:year1>/<int:year2>')
def get_films_years(year1, year2):
    films = get_by_years(year1, year2)
    return jsonify(films)


@app.route('/rating/children')
def films_for_kids():
    films = rating_children()
    return jsonify(films)


@app.route('/rating/family')
def films_for_family():
    films = rating_family()
    return jsonify(films)


@app.route('/rating/adult')
def films_for_adults():
    films = rating_adult()
    return jsonify(films)


@app.route('/genre/<genre>')
def films_by_genre(genre):
    films = get_by_genre(genre)
    return jsonify(films)


app.run()
