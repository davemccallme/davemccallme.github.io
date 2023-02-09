# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:03:28 2019

@author: DavidM
"""

import os 

ATBS = 'C:\Anaconda3\MyPythonScripts\AutomateTheBoringStuff'

for folderName, subfolders, filenames in os.walk(ATBS):
    print('The Folder is ' + folderName)
    print('The subfolders in ' + folderName + 'are: ' + str(subfolders) + '/n')
    print('The subfolders in ' + folderName + 'are: ' + str(filenames))
    print()