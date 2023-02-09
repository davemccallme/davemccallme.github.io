# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:40:55 2019

@author: DavidM
"""

#shelve files to store lists and dictionaries

import shelve
shelfFile = shelve.open('mydata')     #returns a shelf file object 
shelfFile['cats'] = ['Donut','Meggy', 'SugarBaby', 'Sheba/GreyCat','Lily', 'Ginger', 'ShadowCat/Shamrock']
shelfFile.close()

