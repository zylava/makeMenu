from database_setup import db, Recipe, Description

description_1 = Description(description='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', recipe_name='Mapo')

description_2 = Description(description='bbbbbbbbbbbbbbbbbbbbbbbbbbbb', recipe_name='Hongshao')
description_3 = Description(description='ccccccccccccccccccc', recipe_name='Jiaozi')

db.session.add(description_1)
db.session.add(description_2)
db.session.add(description_3)

db.session.commit()
