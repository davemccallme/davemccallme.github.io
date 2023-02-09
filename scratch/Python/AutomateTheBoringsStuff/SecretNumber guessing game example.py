#how to automate the boring stuff lesson 12
#This program is a "Guess the Number Game!"


###Imports####
import random

###Definitions###

def start():
    #guessesTaken = 1 #resets guesses to 1 
    print('New Game!')    


def guessAgain():
    print('That guess is too')
    
       
def correctguess():
    print('You got it '+ name +'!! That\'s some damn good guessin\'!')

def validationCheck():
    print('that is not a number in my world')

 
  


#####Start######

#replay = "Y"
#while replay == "Y" or "y":
print('Hello there! Let\'s play a guessing game!')
print('What is your name?')
name = 'Dave' #input()

print('Well ' + name + ', I am thinking of a number between 1 and 20')
secretNumber = random.randint(1,20)         #assigns the secret # for the game

print('(Debug) (' + secretNumber + ') is the secret number!'


# Ask the player to guess 6 times
for guessesTaken in range(1, 7):         #number of guesses player can take
    print('take a guess')
    guess = int(input())

    if guess > secretNumber:            #too high
        print(str(guessAgain) + 'high')
        print('try again')
        

    elif guess < secretNumber:          #too low
        print(str(guessAgain) + 'low')                      #new number
        print('give it another go')
        
    else:
        break                           #This is for a correct guess or error

if guess == secretNumber:
    correctguess()
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

print('Play again? Y/N')
replay = input()
    if replay != "Y" or "y" or "yes" or "YES" or "Yes" or "YEs" or "YeS":
        start()

    else:
        print('Thanks for playing! Goodbye!')

    
    
    
    
