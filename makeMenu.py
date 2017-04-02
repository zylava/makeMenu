# To make HTTP requests easier
import requests

from flask import Flask, request, redirect, url_for, flash, render_template, \
                  make_response, session as login_session
from flask.json import jsonify, loads

from sqlalchemy.orm.exc import NoResultFound
from database_setup import app, db, Recipe, Ingredient, Description

from form import MyForm

from match_ingredients import matchRecipe

@app.route('/catalog/<string:recipe_name>/ingredients/')
def ingredients_of_recipe(recipe_name):
	recipes = Recipe.query.order_by(Recipe.name)
	recipe = Recipe.query.filter_by(name=recipe_name).one()
	return render_template(
                          'ingredients_of_recipe.html',
                          recipes=recipes,
                          recipe=recipe
                          )

@app.route('/catalog/<string:recipe_name>/<string:ingredient_name>/')
def show_ingredient(recipe_name, ingredient_name):
    ingredient = Ingredient.query.filter_by(name=ingredient_name).one()
    return render_template('show_ingredient.html', ingredient=ingredient)

@app.route('/catalog/add/', methods=['GET', 'POST'])
def query_for_recipe():
    form = MyForm()
    if form.validate_on_submit():
        ingredients = form.ingredients.data
        user_list = [str(w).strip() for w in ingredients.split(',')]
	    #print user_list
        print(user_list)
        recipes = Recipe.query.order_by(Recipe.name)
        recipe_to_ingredient_map = {}
        for recipe in recipes:
            ingre_list = [str(ingre.name) for ingre in recipe.ingredients]
            recipe_to_ingredient_map[str(recipe.name)] = ingre_list
	print "map: "
    	print recipe_to_ingredient_map
        #print(recipe_to_ingredient_map)
        (dishes,incomplete_dishes) = matchRecipe(user_list, recipe_to_ingredient_map)
	print "dishes: "
        print(dishes)
	print "incomplete dishes: "
        print(incomplete_dishes)
        return render_template('prompt.html',
                                recipe_list=dishes,
				incomplete_recipe_list=incomplete_dishes
                                )


    if request.method == "POST":
        if not (form.description.data):
            flash("You have to fill name and description about the ingredient.")

    return render_template('add_or_edit_ingredient.html', form=form)

@app.route('/')
@app.route('/catalog/')
def homepage():
    recipes = Recipe.query.order_by(Recipe.name)
    return render_template(
                          'homepage.html',
                          recipes=recipes
                          )



if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'not_secret_at_all'
    app.run(host='0.0.0.0', port=8000)
