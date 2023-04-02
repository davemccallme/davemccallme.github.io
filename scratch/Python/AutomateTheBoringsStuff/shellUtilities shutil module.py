# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:54:39 2019

@author: DavidM
"""


myFile = ('C:\Anaconda3\MyPythonScripts\AutomateTheBoringStuff\spam.txt')

spamFile = open(myFile, 'w')                       #open file in write mode
spamFile.write('Spam (   ^  _  ^   )<--    '*3)    #writes text into file
spamFile.close()                                    #close file


import shutil  #shell utilities module - copy move rename and delete files 
shutil.copy(myFile, 'C:\Anaconda3\MyPythonScripts\\spam_backup.txt')   #copies and renames file