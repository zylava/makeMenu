from database_setup import db, Recipe, Ingredient

ingredient_1 = Ingredient(name='tofu', description='TOFU', recipe_name='Mapo')

ingredient_2 = Ingredient(name='green onion', description='GREEN ONION', recipe_name='Mapo')
ingredient_3 = Ingredient(name='black pepper', description='BLACK PEPPER', recipe_name='Mapo')

db.session.add(ingredient_1)
db.session.add(ingredient_2)
db.session.add(ingredient_3)

db.session.commit()
