# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:07:26 2019

@author: DavidM
"""

#Traffic similator program with
#interstections and stoplights

market_2nd = {'ns': 'green', 'ew':'red'}  #represents stopslights data structure 
                                          # ns = north south , ew = east west 

#create a funstion that will switch the lights
def switchLights(intersection):
    for key in intersection.key():         # run the same switching code on ns as ew
        if intersection[key] == 'green':   # if set to green
            intersection[key] = 'yellow'   # switch to yellow, if yellow set...
        elif intersection[key] == 'red':   # ...to red and if light is red
            intersection[key] =  'g        # set to green
     
        
    print(market_2nd)    
    switchLights(market_2nd)
    print(market_2nd)
    