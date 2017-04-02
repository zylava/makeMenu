#!/usr/bin/env python

import sys
#for line in sys.path:
#    print line
#    print "--------------"
sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages")
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from recipeKeeper import recipeKeeper
import signal

# Get directory of this file
fileDir = os.path.dirname(os.path.realpath(__file__))

# Initialize recipe keeper and crawler
myRecipeKeeper = recipeKeeper(fileDir+"/recipeList.txt")

def signal_handler(signal, frame):
        print('You pressed Ctrl+C! Saving already crawled!')
	myRecipeKeeper.save()
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

myRecipeKeeper.crawl()
#myRecipeKeeper.display()
myRecipeKeeper.save()




