#break statement goes to the next line during a loop
#continue returns to the top of the loop
# ctrl + [ or ] indents blocks of code

#this program checks for valid name entry
#then this program demonstrates the range function in a for loop


print('please enter a name')
name = 'dave' #input()                          #prompt user for name entry
                     
'''while name != int(name):                #bool name validation check, loop until non numerical string is entered
    print('you did not enter a name')
    print('please try again')
    name = input()                      #re-entry 
  
    while name == ' ':              #check for blank entry
        print('you did not enter a name')
        print('please try again')
        name = input()              #reprompt for user name

print('this section is good to go')
'''


#For loop
print('my name is')
for i in range(3):
    print(name +' '+ str(i))
for i in range (-5, 5):
    print(name + ' ' + str(i))
for i in range (10, -10, -2):
    print(name + ' ' + str(i))
print('Done')
