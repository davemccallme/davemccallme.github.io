#this program is index method practice for lists

spam = ['hi', 'yo', 'what\'s up'] #this must be a list [] not a string()
print(spam)
print(spam.index ('yo'))        #returns the position in the list of the value

spam.append ('wassup')          #append method adds to end of list
print(spam)

spam.insert(3, 'Yolo')          #insert within a list
print(spam)


spam.remove('hi')               #finds the value in list and removes
print(spam)

del spam[1]                     #deletes the item at specified index location
print(spam)


spam.sort()                     #sorts in ASCII-betical order (ABC,abc)
print(spam)


spam.sort(key=str.lower)        #sorts in ALPHAbetical order (Aa,Bb,Cc)
print(spam)

spam.sort(reverse=True)         #reverse order
print('rewind!!! ')

for i in range(len(spam)):      #loops length of list spam
        print(str(spam[i]) + ' is listed as ' + str(i))
