from flask_sqlalchemy import SQLAlchemy
from config import app

db = SQLAlchemy(app)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    malls = db.relationship('Mall', backref='account', lazy=True)

    def __repr__(self) -> str:
        return f"Account(name = {self.name})"


class Mall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey(
        'account.id'), nullable=False)
    units = db.relationship('Unit', backref='mall', lazy=True)

    def __repr__(self) -> str:
        return f"Mall(name = {self.name})"


class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mall_id = db.Column(db.Integer, db.ForeignKey('mall.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Unit(name = {self.name})"


db.create_all()
