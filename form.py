from database_setup import Recipe

categories = Recipe.query.order_by(Recipe.name)
recipe_choices = [(recipe.name, recipe.name) for recipe in categories]
recipe_choices = recipe_choices

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Regexp, Length

class MyForm(FlaskForm):
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    submit = SubmitField('Submit')
