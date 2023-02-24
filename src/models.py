from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)
    tabla_Favorites = db.relationship('Favorites', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
            # do not serialize the password, its a security breach
        }    

class Personaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    tabla_Favorites = db.relationship('Favorites', backref='personaje', lazy=True)

    def __repr__(self):
        return '<Personaje %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
            # do not serialize the password, its a security breach
        }    
    

    
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    tabla_Favorites = db.relationship('Favorites', backref='vehicle', lazy=True)
    
    def __repr__(self):
        return '<Vehicle %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
            # do not serialize the password, its a security breach
        }        

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    tabla_Favorites = db.relationship('Favorites', backref='planet', lazy=True)

    def __repr__(self):
        return '<Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
            # do not serialize the password, its a security breach
        }                

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    iduser= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    idpersonaje = db.Column(db.Integer, db.ForeignKey("personaje.id"), nullable=False)
    idplanet = db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=False)
    idvehicle = db.Column(db.Integer, db.ForeignKey("vehicle.id"), nullable=False)
    
    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user": self.iduser,
            "personaje": self.idpersonaje,
            "planet": self.idplanet,
            "vehicle":self.idvehicle
            # do not serialize the password, its a security breach
        }    
        

   
    
    

    