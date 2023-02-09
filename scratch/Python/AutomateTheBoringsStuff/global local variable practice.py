#this program is practice for global and local scopes


spam = 42 # this is a global variable

def eggs():
    spam = 24 # this is a local variable
    print (str(spam) + ' is local and')
    spam += 1
    print(str(spam) + ' is the new local variable')

print(str(spam) + ' is a global while ')
eggs()
spam = 43

print(str(spam) + ' is the new global')
