from database_setup import db, Recipe, Ingredient

recipe_1 = Recipe(name='Mapo')
recipe_2 = Recipe(name='Hongshao')
recipe_3 = Recipe(name='Jiaozi')

db.session.add(recipe_1)
db.session.add(recipe_2)
db.session.add(recipe_3)

db.session.commit()
