from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    iduser = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    tabla_Favorites = db.relationship('Favorites', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.iduser
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }    

# class Personaje(db.Model):
#     idpersonaje = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), unique=True, nullable=False)
    
#     def __repr__(self):
#         return '<Personaje %r>' % self.idpersonaje
    
# class Planet(db.Model):
#     idplanet = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), unique=True, nullable=False)
#     def __repr__(self):
#         return '<Planet %r>' % self.idplanet
# class Vehicle(db.Model):
#     idvehicle = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), unique=True, nullable=False)
#     def __repr__(self):
#         return '<Vehicle %r>' % self.idvehicle

class Favorites(db.Model):
    idfav       = db.Column(db.Integer, primary_key=True)
    iduser      = db.Column(db.Integer, db.ForeignKey("User.iduser", nullable=False))
    idpersonaje = db.Column(db.Integer, db.ForeignKey("Personaje.idpersonaje"))
    idplanet    = db.Column(db.Integer, db.ForeignKey("Planet.idplanet"))
    idvehicle   = db.Column(db.Integer, db.ForeignKey("Vehicle.idvehicle"))
    
    def __repr__(self):
        return '<Favorites %r>' % self.idfav

    def serialize(self):
        return {
            "id": self.idfav,
            "usuario": self.iduser,
            
            # do not serialize the password, its a security breach
        }    
    
    
    

    