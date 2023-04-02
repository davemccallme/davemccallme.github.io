# -*- coding: utf-8 -*-
"""
Created on Sat May  4 18:31:20 2019

@author: DavidM
"""
#part 2 of the Automate the boring stuff lesson 40 parsing html the code 

# Web pages are plaintext files formatted as HTML
# HTML can be parsed with BeautifulSoup module
# BeautifulSoup is imported with the name bs4
# pass the string with the HTML to the bs4.BeautifulSoup() function to get a Soup object
# The Soup object has a select() method that can be passed...
# ...a string of the CSS selector for an HTML tag
# You can get a CSS slector string from the browsers developer tools by...
# ...r.clicking the element and selecting Copy CSS Path
# The select() method will return a list of mathcing ELements objects


######################## Start ###########################################
# Web pages are plaintext files formatted as HTML
# BeautifulSoup is imported with the name bs4    
# HTML can be parsed with BeautifulSoup module
import bs4, requests 

def getQuotesfromweb(SiteUrl):
    res = requests.get(SiteUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
# The select() method will return a list of mathcing ELements objects
# You can get a CSS slector string from the browsers developer tools by...
# ...r.clicking the element and selecting Copy CSS Path
    elems = soup.select('#main > div.w3-panel.w3-info.intro > p:nth-child(1)')               # returns a list of matching elements 
# The Soup object has a select() method that can be passed...
# ...a string of the CSS selector for an HTML tag
    return elems[0].text.strip()
    
# pass the string with the HTML to the bs4.BeautifulSoup() function to get a Soup object    
quote = getQuotesfromweb('https://www.w3schools.com/sql/default.asp')  #assigned to SiteURL when getQWebquotes is called

print('This is the websites quote:\n "' + quote + '"'+ '\n' + 'end' )

    
    

############################# Part 1 #################################
'''
import requests
res = requests.get('https://www.w3schools.com/sql/default.asp')
res.raise_for_status()

### Returns object passed HTML text downloaded ###
soup = bs4.BeautifulSoup(res.text, 'html.parser') 
### Returns object passed HTML text downloaded ###

#(user r.click web browser to inspect element,
r.click to get path to HTML w/ 'selector' or 'CSS' path, not xpath)#

### CSS / selector address ##
elems = soup.select('#main > div.w3-panel.w3-info.intro > p:nth-child(1)')  
### CSS / selector address ##

                    
### "SQL is a standard language for storing, manipulating and retrieving data in databases." ###
print(elems[0].text.strip())  
# elems is a "one object list" =[0], strip cleans up spaces in the returned text #
###"SQL is a standard language for storing, manipulating and retrieving data in databases." ###



# string = soup.get_text()
# print(string[0:500])
# main > div.w3-panel.w3-info.intro > p:nth-child(2)  
'''
############################# Part 1 #################################
