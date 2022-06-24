from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(200), unique=True, nullable=False)
    gender = db.Column(db.String(100))
    url = db.Column(db.String(500), unique=True)

    def __repr__(self):
        return '<Characters %r>' % self.character_name

    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_name,
            "gender": self.gender,
            "url": self.url,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(200), unique=True, nullable=False)
    orbit = db.Column(db.String(200))
    url = db.Column(db.String(500), unique=True)

    def __repr__(self):
        return '<Planets %r>' % self.planet_name

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            "orbit": self.orbit,
            "url": self.url,
            # do not serialize the password, its a security breach
        }

class Characters_Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return '<Characters_Favorites %r>' % self.character_name

    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_name,
            # do not serialize the password, its a security breach
        }

class Favorite_Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return '<Favorite_Planets %r>' % self.planet_name

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            # do not serialize the password, its a security breach
        }