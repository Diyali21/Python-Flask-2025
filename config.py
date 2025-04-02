from os import environ

from dotenv import load_dotenv

load_dotenv()

print(environ.get("LOCAL_DATABASE_URL"))


class Config:
    # General pattern
    # mssql+pyodbc://@<server_name>/<db_name>?driver=<driver_name>
    SQLALCHEMY_DATABASE_URI = environ.get("LOCAL_DATABASE_URL")
    SECRET_KEY = environ.get("SECRET KEY")
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False
