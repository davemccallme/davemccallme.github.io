#This program says hello and asks for my name

print('Hello world')
print('what is you name?')
myName = input() #asks for user name
print( 'Hi ' + myName + ' what is your age?') #ask for user age
myAge = input()

if int(myAge) <100 and int(myAge) >= 5:
    print ( 'Well ' + myName + ' you will be ' + str(int(myAge)+1) + \
        ' next year... congratualtions!')
    print ('Done')
elif int(myAge) <5:
    print ( 'Well ' + myName + ' you are too young to code but you will be ' + str(int(myAge)+1) + \
        ' next year... congratualtions!')
