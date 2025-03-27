from flask import Flask, render_template

from routes.main_bp import main_bp
from routes.movies_bp import movies_bp
from routes.movies_list_bp import movies_list_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    # Flask - Blueprints
    app.register_blueprint(movies_bp, url_prefix="/movies")  # Refactor - Mailability ⬆️
    app.register_blueprint(movies_list_bp, url_prefix="/movie-list")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

# Ctrl + ~ -> Open and close terminal
