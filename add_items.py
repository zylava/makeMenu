from database_setup import db, Category, Item

item_1 = Item(name='tofu', description='TOFU', category_name='Mapo')

item_2 = Item(name='green onion', description='GREEN ONION', category_name='Mapo')
item_3 = Item(name='black pepper', description='BLACK PEPPER', category_name='Mapo')

db.session.add(item_1)
db.session.add(item_2)
db.session.add(item_3)

db.session.commit()
