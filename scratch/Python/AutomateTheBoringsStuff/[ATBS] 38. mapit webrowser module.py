# -*- coding: utf-8 -*-
"""
Created on Fri May  3 18:31:55 2019

@author: DavidM
"""
#### This program is used to launch google maps to an entered address from cmd line  ###### 

# Ref lesson 22 for launching batch files from cmd line


import webbrowser , sys, pyperclip

sys.argv # sys.argv passers command line argumemnts to the script ['mapit.py', '870', 'Valencia', 'St.']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.']  -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])     #slice to convert to single string value stored in address variable
else:
    address = pyperclip.paste()  # in case address is held in clipboard 
    
    # URL: https://www.google.com/maps/place/870+Valencia+St,+San+Francisco,+CA+94110/@37.7589579,-122.4238514,17z/data=!3m1!4b1!4m5!3m4!1s0x808f7e3dae0fc797:0x26acf7c8a5797e94!8m2!3d37.7589579!4d-122.4216627
    # URL Modified: https://www.google.com/maps/place/870 Valencia St San+Francisco CA   <-- this shortcut takes you to same as line above URL 
    
    #URL = 'https://www.google.com/maps/place/' + ADDRESS
webbrowser.open('https://www.google.com/maps/place/' + address)


### mapit.bat script sample
'''@echo off
py.exe C:\Anaconda3\MyPythonScripts\AutomateTheBoringStuff\mapit.py %*    # %* forwards cmd arguments to script
pause'''
