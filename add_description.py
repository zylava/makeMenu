from database_setup import db, Recipe, Description

description_1 = Description(description='Whisk together soy sauce, sesame oil, olive oil, vinegar, peanut butter, cayenne pepper, ginger, garlic, and serrano in a small bowl; set aside. Toast spelt kernels in a dry skillet on medium-high heat until the kernels are browned and some have popped. Remove, place in a mesh strainer, and rinse well with cold water. Drain. Bring 6 cups of water to a boil in a large saucepan; add 1/2 teaspoon kosher salt and stir in spelt kernels. Return to a boil then cover, reduce heat to low, and simmer until tender, about 1 hour. Drain well and set aside to cool. While the spelt is simmering, fill a skillet with 1 quart water, 1/2 teaspoon salt, and onion. Bring to a boil over high heat. Add chicken breasts, reduce the heat to medium-low, cover, and simmer until the chicken is cooked through, about 15 minutes. Remove chicken from liquid and allow to cool. Once chicken is cool enough to handle, shred into bite-sized chunks and place in a large bowl. Stir in spelt, bell pepper, green onions, parsley, cilantro, carrots, and cabbage. Pour sauce over salad and stir well to combine.', recipe_name='Spicy Chicken and Spelt Salad')

description_2 = Description(description='Preheat oven to 350 degrees F (175 degrees C). Combine the seasoning, salt, mustard powder, garlic powder and black pepper; set aside. Rinse the chicken thoroughly, and remove the giblets. Place chicken in a 9x13 inch baking dish. Sprinkle 1 1/2 teaspoons of the spice mixture inside the chicken. Rub the remaining mixture on the outside of the chicken. Squeeze the juice of the 2 lemons into a small bowl or cup, and mix with the olive oil. Drizzle this oil/juice mixture over the chicken. Bake in the preheated oven for 1 1/2 hours, or until juices run clear, basting several times with the remaining oil mixtur', recipe_name='Lemon Herb Chicken')

description_3 = Description(description='Mix peas, green beans, corn, onion, celery, salt, and pepper together in a bowl. Combine sugar, oil, and vinegar in a saucepan over medium heat; cook and stir until sugar is dissolved, about 5 minutes. Pour mixture over vegetable mixture and stir to coat; refrigerate until flavors blend, 8 hours to overnight.', recipe_name='Vegetable Salad')

db.session.add(description_1)
db.session.add(description_2)
db.session.add(description_3)

db.session.commit()
