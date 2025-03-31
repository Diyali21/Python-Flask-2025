import uuid

from extensions import db


# user - id, username, password
# create
class User(db.Model):
    __tablename__ = "movies"
    id = db.Colum(
        db.String(50), primary_key=True, default=lambda: str(uuid.uuid4())
    )  # converting uuid into str -> uuid4 vs uuis1 -> as number increases, the randomness increases
    username = db.Column(db.String(100))
    password = db.Column(db.String(255))

    def to_dict(self):
        return {"id": self.id, "username": self.username, "password": self.password}
