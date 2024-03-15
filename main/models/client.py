from database.db import db

class Cliente(db.Model):
    __tablename__ = "cliente"

    id = db.Column(db.INTEGER, primary_key = True)
    nome = db.Column(db.VARCHAR(30), nullable = False)
    sobrenome = db.Column(db.VARCHAR(100), nullable = False)
    telefone = db.Column(db.CHAR(11), nullable = False)
    email = db.Column(db.VARCHAR(100), nullable = False)
    user = db.relationship("Usuario", back_populates = "cliente")
    endereco = db.relationship("Endereco", back_populates = "cliente")