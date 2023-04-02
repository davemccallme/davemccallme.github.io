# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Automate the Boring Stuff Lesson 39: Downloading from the web with Requests Module
#Pages 207-240 Textbook

#use requests modules when you have the exact url to download, use selenium for variable urls

# Start #

url = 'https://www.goodreads.com/quotes'

###Try/except allows program to continue running even with failed download###
try:
    res = requests.get(url)      # Download files from the web with 'requests' module
                                # Returns response object module diognoses data on the url returned 
except:
    res.raise_for_status()   # raises exception at time of error, ensures program halts if failed download
                    
'''
print(res.status_code)       # checks if response succeeded with response object
                             # ex. value 404 = error, value 200 = succeeded
print(len(res.text))         # res.text holds the string in requests module
                             #show count of string
print(res.text[:50])
'''
### Unicode below: learn more at http://bit.ly/unipain or https://nedbatchelder.com/text/unipain.html###
### make a byte string (what type of encoding is it? check the protocol, 
### or unicode string, the final coding for text for all language and symbols ###
### facts of life summary for bytes and Unicode encoding ###
    #1 ALL data is transfered as 1/0 bytes 
    #2 bytes is limited to 256 char and we need more
    #3 we need both unicdoe and bytes
    #4 we cannot choose we must do both encodings
    #5 declaared encodings can be wrong
    #PRO TIP# 
    #1  Write code as unicode sandwhich [bytes -unicode - bytes]
    #2 Know what kind of strings you are deailing with: bytes? or unicode?
    #3 test, test, test

playFile = open('goodreads.com_quotes.txt', 'wb')  #wb = write binary mode instead of text to maintain unicode
                                                            # open =  returns file object, saves to file
for chunk in res.iter_content(100000):                  #save file to drive with iter_content method
    playFile.write(chunk)

playFile.close()


# learn about other requests modules at 'requests.readthedocs.org'