class Config:
    # General pattern
    # mssql+pyodbc://@<server_name>/<db_name>?driver=<driver_name>
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://@PF463819\SQLEXPRESS/SanlamMovieDB2025?driver=ODBC+Driver+17+for+SQL+Server"
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False
