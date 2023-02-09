# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:19:06 2019

@author: DavidM
"""

#Box printing function

"""


*******************
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*******************


"""

#create any size box

w = 2
h = 2    

def boxPrint(symbol, width, height):
    print(symbol * width)
    if len(symbol) != 1:
        raise Exception('symbol needs to be a string length of 1.')
    if (width < 2) or (height <2):
        raise Exception('box size must be greater than 1 ')



    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    
    print(symbol * width)
    
boxPrint("*", w, h)
boxPrint("+", w +30, h+10)
