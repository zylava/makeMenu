# To make HTTP requests easier
import requests

from flask import Flask, request, redirect, url_for, flash, render_template, \
                  make_response, session as login_session
from flask.json import jsonify, loads

from sqlalchemy.orm.exc import NoResultFound
from database_setup import app, db, Category, Item

from form import MyForm

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
