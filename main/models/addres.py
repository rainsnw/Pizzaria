from database.db import db

class Endereco(db.Model):
    __tablename__ = "endereco"

    id = db.Column(db.INTEGER, primary_key = True)
    rua = db.Column(db.VARCHAR(50), nullable = False)
    bairro = db.Column(db.VARCHAR(50), nullable = False)
    numero = db.Column(db.INTEGER, nullable = False)
    cidade = db.Column(db.VARCHAR(50), nullable = False)
    estado = db.Column(db.CHAR(2), nullable = False)
    cep = db.Column(db.CHAR(8), nullable = False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    cliente = db.relationship("Cliente", back_populates = "endereco")