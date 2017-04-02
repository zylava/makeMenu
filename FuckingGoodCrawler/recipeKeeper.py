#!/usr/bin/env python
__metaclass__ = type

import sys
import urllib2
import urlparse
from bs4 import BeautifulSoup
import socket
import httplib
from pprint import pprint

class recipeKeeper:
    def __init__(self, mapFile):
	self.hdr = {'User-Agent': 'Mozilla/5.0'}
        # Initialize mapping
        self.mapFile = mapFile
        self.map = {}
        # Load existing recipes
        with open(mapFile) as recipeMap:
            entries = recipeMap.read().rstrip('>>>>\n').split('>>>>\n')
            if entries != ['']:
                for entry in entries:
                    # Split entry into dish, ingredients and directions
                    itemGroup = entry.split('####\n')
                    dish = itemGroup[0].strip()
                    self.map[dish] = []
                    self.map[dish].append([])
                    # Save ingredients
                    for ingredient in itemGroup[1].strip(' ').strip('\n').split('\n'):
                        if not ingredient.isspace():
                            (self.map[dish])[0].append(ingredient.strip())
                    # Save directions
                    self.map[dish].append([])
                    for direction in itemGroup[2].strip(' ').strip('\n').split('\n'):
                        if not direction.isspace():
                            (self.map[dish])[1].append(direction.strip())

    def crawl(self):
        base_url = "http://www.recipe.com/"
        page = self.getPage(base_url)
        lists = page.find(class_='dropdown').find_all('li')
        for listItem in lists:
            print ''
            url = listItem.find('a').get('href')
            page = self.getPage(url)
            # Find recipe class
            recipe_markups = page.find_all("div", class_='recipe')
            for recipe_markup in recipe_markups:
                # Find urls to recipes
                link = recipe_markup.find('h3').find('a')
                recipe_url = link.get('href')
                dish = link.get_text()
                # Add recipes not already have
                if dish not in self.map:
                    page = self.getPage(recipe_url)
                    self.processRecipePage(page, dish)

    def display(self):
        print "\n\n\n\n\ndisplay starts\n"
        for key, val in self.map.iteritems():
             print key, val[0], val[1]
#            print key, "\n"
#            print "Ingredients:>>>>>>>>>>>>>>>>>>>>>\n"
#            for ingredient in val[0]:
#                print ingredient, '\n'
#            print "Directions:>>>>>>>>>>>>>>>>>>>>>\n"
#            for direction in val[1]:
#                print direction, '\n'

    def save(self):
        print "saving!!!"
        with open(self.mapFile, 'w') as recipeMap:
            for key, val in self.map.iteritems():
                recipeMap.write(key+'\n')
                recipeMap.write('    ####\n')
                for ingredient in val[0]:
                    recipeMap.write('    '+ingredient+'\n')
                recipeMap.write('    ####\n')
                for direction in val[1]:
                    recipeMap.write('    '+ direction +'\n')
                recipeMap.write('>>>>\n')
        print "saved!!!!"

    def getPage(self, url):
        req = urllib2.Request(url,headers=self.hdr)
        try:
            response = urllib2.urlopen(req)
            print "Processing: ", url
        except (UnicodeEncodeError, urllib2.HTTPError, urllib2.URLError, socket.error, httplib.BadStatusLine), e:
                print "Error when opening url -> "+ url +": ", e
        page = BeautifulSoup(response, "lxml")
        return page
                
    def processRecipePage(self, page, dish):
        # Find correct ingredients markup
        ingredients_markup = page.find(class_="ingredients")
        if ingredients_markup is None:
            ingredients_markup = page.find(class_="recipe__ingredientContainer")
        if ingredients_markup is not None:
            # Find and add ingredients
            recipe = []
            recipe.append([])
            for list_item in ingredients_markup.find_all('li'):
                if not list_item.get_text().isspace():
                    recipe[0].append(list_item.get_text().replace('\n', ' ').replace('  ', ' ').strip(' '))
            # Find correct directions markup
            directions_markup = page.find(class_="directions")
            if directions_markup is None:
                directions_markup = page.find(class_="direction")
            if directions_markup is None:
                directions_markup = page.find(class_="recipe__directionsContainer")
            if directions_markup is not None:
                # Find and add directions
                recipe.append([])
                for list_item in directions_markup.find_all('li'):
                    if not list_item.get_text().isspace():
                        recipe[1].append(list_item.get_text().replace('\n', ' ').replace('  ', ' ').strip(' '))
                # store recipe
                self.map[dish] = recipe
            else:
                print "processing failed"
        else:
            print "processing failed"

        
