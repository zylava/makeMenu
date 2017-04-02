from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ingredient_catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Recipe(db.Model):
    __tablename__ = 'recipe'

    name = db.Column(db.String(80), primary_key=True)

class Description(db.Model):
	__tablename__ = 'description'

	description = db.Column(db.String(500), primary_key=True)
	recipe_name = db.Column(db.String, db.ForeignKey('recipe.name'))
	recipe = db.relationship(
                           'Recipe',
                           backref=db.backref('description')
                              )

	@property
	def serialize(self):
		return {
			'description': self.description,
			'recipe_name': self.recipe_name
		}

class Ingredient(db.Model):
    __tablename__ = 'ingredient'

    name = db.Column(db.String(80), primary_key=True)
    recipe_name = db.Column(db.String, db.ForeignKey('recipe.name'))

    recipe = db.relationship(
                           'Recipe',
                           backref=db.backref('ingredients')
                              )

    @property
    def serialize(self):
        return {
                'name': self.name,
                'recipe_name': self.recipe_name
               }

db.create_all()
