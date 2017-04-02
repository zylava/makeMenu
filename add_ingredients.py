from database_setup import db, Recipe, Ingredient

ingredient_1 = Ingredient(name='tofu', recipe_name='Mapo')

ingredient_2 = Ingredient(name='green onion', recipe_name='Mapo')
ingredient_3 = Ingredient(name='black pepper', recipe_name='Mapo')

db.session.add(ingredient_1)
db.session.add(ingredient_2)
db.session.add(ingredient_3)

db.session.commit()
