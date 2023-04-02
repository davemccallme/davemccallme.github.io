secretNumber = 10
def guessAgain():
    print('that number is too ')
# Ask the player to guess 6 times
for guessesTaken in range(1, 7):         #number of guesses player can take
    print('take a guess')
    guess = int(input())

    if guess > secretNumber:            #too high
        print(guessAgain + 'high')
        print('try again')
        

    elif guess < secretNumber:          #too low
        print(guessAgain + 'low')                      #new number
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

    
    
    
    
