from database.db import db

class Pizza(db.Model):
    __tablename__ = "pizza"

    id = db.Column(db.INTEGER, primary_key = True)
    sabor = db.Column(db.VARCHAR(100), nullable = False)
    borda = db.Column(db.VARCHAR(100), nullable = False)
    topping = db.Column(db.VARCHAR(100), nullable = True)
    cobertura = db.Column(db.VARCHAR(100), nullable = True)
    tamanho = db.Column(db.VARCHAR(50), nullable = False)
    preco = db.Column(db.FLOAT(precision = 2), nullable = False)
    number_of_pizza = db.relationship("Qntd_Pizzas", back_populates = "pizza")