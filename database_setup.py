from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///item_catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Category(db.Model):
    __tablename__ = 'category'

    name = db.Column(db.String(80), primary_key=True)


class Item(db.Model):
    __tablename__ = 'item'

    name = db.Column(db.String(80), primary_key=True)
    description = db.Column(db.Text, nullable=False)
    category_name = db.Column(db.String, db.ForeignKey('category.name'))

    category = db.relationship(
                           'Category',
                           backref=db.backref('items')
                              )

    @property
    def serialize(self):
        return {
                'name': self.name,
                'description': self.description,
                'category_name': self.category_name
               }

db.create_all()
