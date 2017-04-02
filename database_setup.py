from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipe_catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Recipe(db.Model):
    __tablename__ = 'recipe'

    name = db.Column(db.String(80), primary_key=True)

class Description(db.Model):
	__tablename__ = 'description'

	description = db.Column(db.String(5000), primary_key=True)
	recipe_name = db.Column(db.String, db.ForeignKey('recipe.name'))
	recipe = db.relationship(
                           'Recipe',
                           backref=db.backref('description')
                              )

class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    recipe_name = db.Column(db.String, db.ForeignKey('recipe.name'))

    recipe = db.relationship(
                           'Recipe',
                           backref=db.backref('ingredients')
                              )

db.create_all()
