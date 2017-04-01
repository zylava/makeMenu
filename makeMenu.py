# To make HTTP requests easier
import requests

from flask import Flask, request, redirect, url_for, flash, render_template, \
                  make_response, session as login_session
from flask.json import jsonify, loads

from sqlalchemy.orm.exc import NoResultFound
from database_setup import app, db, Category, Item

from form import MyForm

@app.route('/catalog/<string:category_name>/items/')
def items_of_category(category_name):
    categories = Category.query.order_by(Category.name)
    category = Category.query.filter_by(name=category_name).one()
    return render_template(
                          'items_of_category.html',
                          categories=categories,
                          category=category
                          )

@app.route('/catalog/<string:category_name>/<string:item_name>/')
def show_item(category_name, item_name):
    item = Item.query.filter_by(name=item_name).one()
    return render_template('show_item.html', item=item)

@app.route('/catalog/add/', methods=['GET', 'POST'])
def add_item():
    form = MyForm()
    if form.validate_on_submit():
        description = form.description.data
	user_list = [str(w).strip() for w in description.split(',')]
	categories = Category.query.order_by(Category.name)
	recipe_to_ingredient_map = {}
	for recipe in categories:
		ingre_list = [str(ingre.name) for ingre in recipe.items]
		recipe_to_ingredient_map[str(recipe.name)] = ingre_list
	print recipe_to_ingredient_map
	return redirect(url_for('homepage'))
	

    if request.method == "POST":
        if not (form.description.data):
            flash("You have to fill name and description about the item.")            

    return render_template('add_or_edit_item.html', form=form)

@app.route('/')
@app.route('/catalog/')
def homepage():
    categories = Category.query.order_by(Category.name)
    return render_template(
                          'homepage.html',
                          categories=categories
                          )



if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'not_secret_at_all'
    app.run(host='0.0.0.0', port=8000)
