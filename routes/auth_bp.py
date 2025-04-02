from pprint import pprint

from flask import Blueprint, redirect, render_template, request, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from extensions import db
from models.user import User

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.get("/login")
def login_page():
    return render_template("login.html")


@auth_bp.post("/login")
def submit_login_page():
    username = request.form.get("username")
    password = request.form.get("password")  # abc@123
    try:
        # 🛡️ Validations
        if not username:
            raise ValueError("Username must be filled")

        if not password:
            raise ValueError("Password must be filled")

        # Select * from users
        #   where username = 'Ethan'
        #   Limit 1;
        user_from_db = User.query.filter_by(username=username).first()

        print(user_from_db)

        if not user_from_db:
            raise ValueError("Credentials are invalid")

        if not check_password_hash(user_from_db.password, password):
            raise ValueError("Credentials are invalid")

        return redirect(url_for("movies_list_bp.movie_list_page"))

    except Exception as e:
        print(e)
        db.session.rollback()
        return redirect(url_for("auth_bp.submit_login_page"))


@auth_bp.get("/signup")
def signup_page():
    return render_template("signup.html")


@auth_bp.post("/signup")
def submit_signup_page():
    username = request.form.get("username")
    password = request.form.get("password")
    confirm = request.form.get("confirm")
    try:
        # 🛡️ Validations
        if not username:
            raise ValueError("Username must be filled")

        if not password:
            raise ValueError("Password must be filled")

        if password != confirm:
            raise ValueError("Password does not match")

        # Only when all validation passes
        hashed_password = generate_password_hash(password)
        data = {
            "username": username,
            "password": hashed_password,
        }

        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        # Todo: Take them to login page
        return redirect(url_for("auth_bp.login_page"))
    except Exception as e:
        print(e)
        db.session.rollback()
        return redirect(url_for("auth_bp.submit_signup_page"))
