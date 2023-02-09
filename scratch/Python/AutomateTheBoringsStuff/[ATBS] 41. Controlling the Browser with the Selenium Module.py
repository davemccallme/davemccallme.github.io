# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:02:07 2019

@author: DavidM
"""
#part 2 of the Automate the boring stuff 
# lesson 41 Controlling the Browser with the Selenium Module
#[ATBS] Pagse 256 261

#Lauches web broswer, find html, fill out forms, clicks submit buttons etc. 
from selenium import webdriver
import os

website = 'https://www.udemy.com/'

gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
browser = webdriver.Firefox()    # Returns a webrowser object that you can programatically control
#control the webrowser with methods#
browser.get(website)
elem = browser.find_element_by_css_selector('span.input-group:nth-child(4)')
elem.click()
elems = browser.find_elements_by_css_selector('p')  #this is plural elements (finds all matches) v element (finds first match)
len(elems)
searchElem = browser.find_element_by_css_selector('.search-field')
searchElem.submit()
                                                 
#browser.back(),forward(),refresh(),quit()
elem.text