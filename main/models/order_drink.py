from database.db import db

class Bebida_pedida(db.Model):
    __tablename__ = "bebida_pedida"

    id = db.Column(db.INTEGER, primary_key = True)
    quantidade = db.Column(db.INTEGER, nullable = False)
    drink_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    drink = db.relationship("Bebida", back_populates = "bebida_pedida", lazy = "dynamic")