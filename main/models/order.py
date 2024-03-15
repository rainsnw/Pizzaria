from database.db import db
from sqlalchemy import DateTime

class Pedido(db.Model):
    __tablename__ = "pedido"

    id = db.Column(db.INTEGER, primary_key = True)
    data_pedido = db.Column(db.DATETIME)
    total = db.Column(db.FLOAT(precision = 2), nullable = False)
    pagamento_id = db.Column(db.Integer, db.ForeignKey('pagamento.id'))
    bebida_pedida_id= db.Column(db.Integer, db.ForeignKey('bebida_pedida.id'))
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    qntd_pizzas_id = db.Column(db.Integer, db.ForeignKey('qntd_pizzas.id'))

    payment = db.relationship("Pagamento", back_populates = "pedido", lazy = "dynamic")
    order_drink = db.relationship("Bebida_pedida", back_populates = "pedido", lazy = "dynamic")
    client = db.relationship("Cliente", back_populates = "pedido", lazy = "dynamic")
    number_pizza = db.relationship("Qntd_Pizza", back_populates = "pedido", lazy = "dynamic")