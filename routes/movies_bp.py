from pprint import pprint

from flask import Blueprint, request

from extensions import db
from models.movie import Movie

# 1. Organize
# 2. app needs to be in main.py
movies_bp = Blueprint("movies_bp", __name__)


# Backend Developer
# /movies -> movies
@movies_bp.get("/")
def get_all_movies():
    # Auto converts data -> JSON (Flask)
    movies = Movie.query.all()  # Select * from movies
    movies_dict = [movie.to_dict() for movie in movies]
    return movies_dict


# /movies/100 - <id> -> Variable
@movies_bp.get("/<id>")
def get_movie_by_id(id):
    # Auto converts data -> JSON (Flask)
    movie = Movie.query.get(id)  # None if no movie

    if not movie:
        return {"message": "Movie not found"}, STATUS_CODE["NOT_FOUND"]

    data = movie.to_dict()
    return data


# /movies/100 - <id> -> Variable
@movies_bp.delete("/<id>")
def delete_movie_by_id(id):  # log
    # Auto converts data -> JSON (Flask)
    movie = Movie.query.get(id)  # None if no movie

    if not movie:
        return {"message": "Movie not found"}, STATUS_CODE["NOT_FOUND"]

    try:
        data = movie.to_dict()
        db.session.delete(movie)  # Error
        db.session.commit()  # Making the change (Update/Delete/Create) # Error
        return {"message": "Movie deleted successfully", "data": data}
    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        return {"message": str(e)}, STATUS_CODE["SERVER_ERROR"]


@movies_bp.post("/")  # HOF
def create_movie():
    data = request.get_json()  # body
    new_movie = Movie(**data)

    try:
        # print(new_movie, new_movie.to_dict())
        db.session.add(new_movie)
        db.session.commit()
        return {
            "message": "Movie created successfully",
            "data": new_movie.to_dict(),
        }, STATUS_CODE["CREATED"]
    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        return {"message": str(e)}, STATUS_CODE["SERVER_ERROR"]


# GET + POST
# /movies/100 - <id> -> Variable
@movies_bp.put("/<id>")
def update_movie_by_id(id):  # id - Which movie
    body = request.get_json()  # body - What data to update

    try:
        updated = Movie.query.filter_by(id=id).update(body)
        print(updated)  # 0 or 1 # No. of rows updated
        if not updated:
            return {"message": "Movie not found"}, STATUS_CODE["NOT_FOUND"]

        db.session.commit()

        updated_movie = Movie.query.get(id)  # Read
        return {
            "message": "Movie updated successfully",
            "data": updated_movie.to_dict(),
        }

    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        return {"message": str(e)}, STATUS_CODE["SERVER_ERROR"]


# 1. filter_by -> where
# 2. update present in filter_by
