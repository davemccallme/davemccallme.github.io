#program demonstrates:
#immutable and mutable values in python

print(list('hello'))

name = 'Donut'              #assign variable
print(list(name))           #show list
print(name[0])              #show first letter of list
print(name[1:3])            #show this "slice"
print(name[-1])             #show the last letter from the list


#strings in python are immutable, they cannot be changed the way integers can

name = 'Donut the Cat'      #name assign
print(name)
newName = (name[:5] + ' McCall')  #string list editing
print(newName)


#variables don't contain lists, they refence lists
#ref lesson 16 how to automate the boring stuff with Python (6:05 mark)
#for more watch https://www.youtube.com/watch?v=_AEJHKGk9ns
