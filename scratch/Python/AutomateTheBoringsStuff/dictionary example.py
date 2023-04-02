#Lesson 17 automate the boring stuff
#https://www.udemy.com/automate/learn/lecture/3465848#content
#This program demsonstrates dictionaries, keys and values


#this is a dictionary, {key1:value1, key2:value2}
#dictionaries have no "order" A-z 1-10, 
myCat = {'size': 'fat', 'color': 'white', 'age': 2, 'name': 'Donut'}      
print(myCat['name'] + ' is ' + myCat['size']\
      + ' and ' + myCat['color'])

print(list(myCat.keys()))   #shows keys
print(list(myCat.values())) #shows vaules
print(list(myCat.items()))  #shows keys paired with values

for Key in myCat.keys():   #for loop lists out each line by line
    print(Key)

for Value in myCat.values():
    print(Value)

for Items in myCat.items():
    print(Items)                #this prints out tuples

print('gender assigned?')
myCat.get('gender', print('Gender not assigned'))  #".get" method returns an exception value if called value is not listed in dictionary

print('now assigning gender')
myCat.setdefault('gender', 'female')                #opposite of ".get" method, sets a value if a key doesn't exist
print(myCat['name'] + ' is ' + myCat['gender']+ '.')



################################################################


import pprint  #clean up string with pretty print function

#assign variable "message"
message = '''Donut is fat and white
['size', 'color', 'age', 'name']
['fat', 'white', 2, 'Donut']
[('size', 'fat'), ('color', 'white'), ('age', 2), ('name', 'Donut')]
size
color
age
name
fat
white
2
Donut
('size', 'fat')
('color', 'white')
('age', 2)
('name', 'Donut')
gender assigned?
Gender not assigned
now assigning gender
Donut is female. '''

#assign variable "count" to become an empty dictionary {}
count = {}  # 'r': 12

for character in message:  #assign a single variable for each letter type in the message
    count.setdefault(character, 0)  #start off at letter 0 to begin count
    count[character] = count[character]+1 #dictionary count with parameter 

pprint.pformat(count)
