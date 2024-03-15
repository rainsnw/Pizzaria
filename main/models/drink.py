from database.db import db

class Bebida(db.Model):
    __tablename__ = "bebida"

    id = db.Column(db.INTEGER, primary_key = True)
    nome = db.Column(db.VARCHAR(100), nullable = False)
    preco = db.Column(db.FLOAT(precision = 2), nullable = False)
    order_drink = db.relationship("Bebida_pedida", back_populates = "bebida")