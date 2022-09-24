import json
import sqlite3


def get_by_title(title):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
        SELECT title, country, release_year, listed_in, description 
        FROM netflix 
        WHERE title LIKE '%{title}%' 
        ORDER BY release_year DESC
""")
        data = cursor.fetchone()
        film = {'title': data[0], 'country': data[1], 'release_year': data[2], 'genre': data[3], 'description': data[4]}
        return film


def get_by_years(year1, year2):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
        SELECT title, release_year
        FROM netflix
        WHERE release_year BETWEEN {year1} AND {year2} AND type = 'Movie'
        LIMIT 100
""")
        data = cursor.fetchall()
        film_list = []
        for i in data:
            films = {'title': i[0], 'release_year': i[1]}
            film_list.append(films)
        return film_list


def rating_children():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
            SELECT title, rating, description
            FROM netflix
            WHERE rating = 'G'
            LIMIT 20
    """)
    data = cursor.fetchall()
    film_list = []
    for i in data:
        films = {'title': i[0], 'rating': i[1], 'description': i[2]}
        film_list.append(films)
    return film_list


def rating_family():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
            SELECT title, rating, description
            FROM netflix
            WHERE rating = 'G' OR rating = 'PG' OR rating = 'PG-13'
            LIMIT 50
    """)
    data = cursor.fetchall()
    film_list = []
    for i in data:
        films = {'title': i[0], 'rating': i[1], 'description': i[2]}
        film_list.append(films)
    return film_list


def rating_adult():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
            SELECT title, rating, description
            FROM netflix
            WHERE rating = 'R' OR rating = 'NC-17'
            LIMIT 50
    """)
    data = cursor.fetchall()
    film_list = []
    for i in data:
        films = {'title': i[0], 'rating': i[1], 'description': i[2]}
        film_list.append(films)
    return film_list


def get_by_genre(genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
            SELECT title, description
            FROM netflix
            WHERE listed_in LIKE '%{genre}%'
            ORDER BY release_year DESC
            LIMIT 10
            
    """)
    data = cursor.fetchall()
    film_list = []
    for i in data:
        films = {'title': i[0], 'description': i[1]}
        film_list.append(films)
    return film_list


def get_by_cast(actor1, actor2):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
            SELECT COUNT(netflix.cast), netflix.cast
            FROM netflix
            WHERE netflix.cast LIKE '%{actor1}%' AND netflix.cast LIKE '%{actor2}%'
            GROUP BY netflix.cast
    """)
    data = cursor.fetchall()
    return data


def find_a_movie(type_, release_year, genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
            SELECT title, description
            FROM netflix
            WHERE type = '{type_}' AND release_year = {release_year} AND listed_in LIKE '%{genre}%'
    """)
    data = cursor.fetchall()
    film_list = []
    for i in data:
        films = {'title': i[0], 'description': i[1]}
        film_list.append(films)
    return json.dumps(film_list)


print(find_a_movie('Movie', 2014, 'horror'))





