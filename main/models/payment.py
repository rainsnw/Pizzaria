from database.db import db

class Pagamento(db.Model):
    __tablename__ = "pagamento"

    id = db.Column(db.INTEGER, primary_key = True)
    formato = db.Column(db.VARCHAR(100), nullable = False)