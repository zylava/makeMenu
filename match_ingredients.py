#!/usr/bin/python

def matchRecipe( items , recipes ):
	"This gives you the minimal amount of ingredients"
	incompleteDishes = {}
	dishes = []
	sorted(items)
	for recipe in recipes:
		if set(recipes[recipe]) <= set(items):
			print "::: " + recipe
			dishes.append(recipe)
		else:
			if len(set(recipes[recipe]) - set(items)) <= 3:
				incompleteDishes[recipe] = list(set(recipes[recipe]) - set(items))
	return (dishes,incompleteDishes)


### Test cases ####

#items = ['onion', 'tofu', 'beef']
#recipes = {'Onion soup': ['onion'], 'Mapo': ['tofu', 'onion'], 'Hongshao': ['pork']}
#recipes = {'Onion soup': ['onion','potato'], 'Burger': ['lettuce','bread','patty'], 'Hongshao': ['pork']}

#items = ['a','b','c','d']
#recipes = {'A':['a','b'], 'B':['a','d'], 'C':['a','b','c','d','e'], 'D':['a','b','c','d','e','f','g','h'], 'E':['c','g','h'],'F':['c','g','h','u','i']}
#recipes = {'C':['a','b','c','d','e'], 'D':['a','b','c','d','e','f','g','h'], 'E':['c','g','h'],'F':['c','g','h','u','i']}

#matchRecipe(items,recipes)
