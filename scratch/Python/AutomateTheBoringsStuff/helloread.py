# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 22:12:21 2019

@author: DavidM
"""

helloFile = open('C:\Anaconda3\MyPythonScripts\Hello.txt')

content = helloFile.read()
print(content)

helloFile = open('C:\Anaconda3\MyPythonScripts\Hello.txt', 'w')    # opens/creates file
helloFile.write('Hello!!!!!!')                                     # write to file
helloFile.write('Hello!!!!!!')                                 
helloFile.write('Helllllllllo!!!!!!')

helloFile.close()                                                  # closes the file

baconFile = open('bacon.txt', 'w')                                 # write mode
baconFile.write('Bacon is not a vegetable.')

baconFile.close()


baconFile = open('bacon.txt', 'a')                                 #  append mode
baconFile.write('\n\nBacon is delicious.')

baconFile.close()

