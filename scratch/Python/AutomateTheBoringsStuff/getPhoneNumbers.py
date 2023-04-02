#! python3


'''
Created on Sun Apr  7 14:48:38 2019

@author: DavidM
'''

import re, pyperclip # re = regular expression method, clipboard copy/paste module


# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000 ext 12345, ext. 12345, x12345
(
	((\d\d\d) | (\(\d\d\d\)))?    # area code (optional) w/ & w/o paren()
	(\s|-)                      # first separator
	\d\d\d                      # first 3 digits
	-      	                    # separator
	 \d\d\d\d                   # last 4 digits
	(((ext(\.)?\s) | x | X)      # extension abr.
	(\d{2,5}))?                  # extensions number (optional)           
)
''', re.VERBOSE)



# Create a regex for email addresses

emailRegex = re.compile(r'''
# some.+_thing@(\d(2,5)))?.com

[a-zA-Z0-9_.+]+   # name part
@                  # @ symbol
[a-zA-Z0-9_.+]+   # domain name part

''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()  # returns the string currently on the clipoard


# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)


allPhoneNumbers = []                             #set variable to list
for phoneNumber in extractedPhone:               
    allPhoneNumbers.append(phoneNumber[0])    


allEmails = []                             # set variable to list
for Email in extractedEmail:               # for loop w/ref
    allEmails.append(Email[0])             # append to list

#print(allPhoneNumbers)                    # debug
#print(extractedPhone)                     # debug
#print(extractedEmail)                     # debug   

#Copy the extracted eamil/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)















