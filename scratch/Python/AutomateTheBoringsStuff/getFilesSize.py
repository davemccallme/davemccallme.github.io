# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 21:43:16 2019

@author: DavidM
"""


# pull the total size of a folder specified
totalSize = 0

# returns a list of strings passed by filename/folder
for filename in os.listdir('C:\Anaconda3\MyPythonScripts\AutomateTheBoringStuff'):  
    if not os.path.isfile(os.path.join('C:\Anaconda3\MyPythonScripts\AutomateTheBoringStuff', filename)):
        continue
    totalSize = totalSize + os.path.join('C:\Anaconda3\MyPythonScripts\AutomateTheBoringStuff')
    