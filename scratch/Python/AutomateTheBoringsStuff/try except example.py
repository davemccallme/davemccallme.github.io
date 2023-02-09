#automate the boring stuff lesson 11
#program tries to handle errors when user does not input positive integer

#code tries to guide user to using the correct values and asks
#for re-entry when errors occur


########Definitions###########
###Responses or number of cats ###
def posiCat():
    global numCats
    try:
        if numCats >= 4:
            print('that\'s a lot of cats')
        elif numCats >0 and numCats <4:
            print('that is not that many cats.')
        elif numCats == 0:
            print('you don\'t have any cats...')
        elif numCats <0:
             print('you did not enter a positive whole number')
            
    #retry after failed attempt
    except:
        print('please try again')
        print('enter a whole number')
        numCats = input()
    
###Function for error checking###
def NumError():
    global numCats

    try:
        int(numCats) == int()
        posiCat()
    except:
        print(numCats)
        print('please try again')
        print('enter a postive whole number')
        numCats = input()
        
        try:
            bool(numCats == abs(int(numCats))) == True
            print('thanks!')
            posiCat()
            #else:
             # while bool(numCats == abs(int(numCats))) == False:
              #  NumError() #repeat error check loop
        except:
            NumError() #repeat error check loop





                
##########    Start Program     #####################
print('How many cats do you have?')
numCats = 'x' #constant for 3.10.19 edit -> "input()" when debugged                           #ask for user input

#Run function
try:
    val = int(numCats) 
except:
    NumError()


print('done')
