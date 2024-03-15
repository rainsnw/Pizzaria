from database.db import db
from database.bcrypt import bcrypt

class Usuario(db.Model):
    __tablename__ = "usuario"
    
    id = db.Column(db.INTEGER, primary_key = True)
    usuario = db.Column(db.VARCHAR(100), unique = True)
    senha = db.Column(db.VARCHAR(100), nullable = False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    cliente = db.relationship("Cliente", back_populates = "usuario", uselist = False)

    def __init__(self, usuario, senha, cliente_id):
        self.usuario = usuario
        self.senha = bcrypt.generate_password_hash(senha)
        self.cliente_id = cliente_id