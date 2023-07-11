from .database import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


class Forum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(100), unique=False, nullable=True)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)
    category = db.relationship('Category',
                               backref=db.backref('forums', lazy=True))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    real_name = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    avatar = db.Column(db.String(100))
    is_admin = db.Column(db.Boolean(), default=False, nullable=False)
    is_active = db.Column(db.Boolean())
