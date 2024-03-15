from database.db import db

class Qntd_Pizzas(db.Model):
    __tablename__ = "qntd_pizzas"

    id = db.Column(db.INTEGER, primary_key = True)
    qntd = db.Column(db.INTEGER, nullable = False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    pizza = db.relationship("Pizza", back_populates = "qntd_pizzas", lazy = "dynamic")