#This is the guess the number game.

import random                                   #random number importer
low = 1                                         #low parameter value
high = 50                                       #high parameter value
CorrectNumber = random.randint(low,high)        #assigns random number within parameters
numGuess = int((high - low)/3 -1)               #amount of guesses allowed 

print('Debug this is the correct number: ' + str(CorrectNumber)) # Debug while building program
print('Welcome to the guess the number game!')
print('I\'m thinking of a number between ' + str(low) + ' and ' + str(high))
print('Take a guess:')


for guess in range(numGuess):
    guess = input()                             #user guesses number
    try:                                        #input validation for integer                
        #If statement here:
        if int(guess) > CorrectNumber and int(guess) < high:
            print('that number is too high, guess again!')  #number too high
     
        elif int(guess) > high:
            print('whoops, please enter guess between ' + str(low) + ' and ' + str(high)) 
     
        elif int(guess) < CorrectNumber and int(guess) > low:
            print('that number is too low, guess again!')   #number too low
     
        elif int(guess) == CorrectNumber:
            print('Correct! That is some good guesssing!')  #number is correct!
            break
        
    except:                                     #for errors when input is not a number 
        print('whoops, please enter guess between ' + str(low) + ' and ' + str(high)) 
print('Done')
