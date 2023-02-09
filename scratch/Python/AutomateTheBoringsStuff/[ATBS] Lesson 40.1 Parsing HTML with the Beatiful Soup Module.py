# -*- coding: utf-8 -*-
"""
Created on Sat May  4 17:01:29 2019

@author: DavidM
"""

#Automate the Boring Stuff 
#40 Parsing HTML with the Beautiful Soup Module

from bs4 import BeautifulSoup        # bs4 = Beautiful soup
import requests
res = requests.get('https://www.w3schools.com/sql/default.asp')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')  #Returns object passed HTML text downloaded

#(user r.click web browser to inspect element, r.click to get path to HTML w/ 'selector' or 'CSS' path, not xpath)
elems = soup.select('#main > div.w3-panel.w3-info.intro > p:nth-child(1)')  # CSS / selector address 

# "SQL is a standard language for storing, manipulating and retrieving data in databases." #
print(elems[0].text.strip())  #elems is a "one object list" =[0], strip cleans up spaces in the returned text

#string = soup.get_text()
#print(string[0:500])
#main > div.w3-panel.w3-info.intro > p:nth-child(2)            

