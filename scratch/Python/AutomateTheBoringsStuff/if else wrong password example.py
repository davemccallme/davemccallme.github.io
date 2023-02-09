#user has 'x' chances to enter correct password to grant access
#else program terminates

#global variables
passwordentries = 1                         #start for # of attempts allowed from user
x=3                                         #the # of password entries before shutdown
correctpassword = 'swordfish'               #program defined correct password
password = ' '                              #reset password entry to blank

while (passwordentries <= x and password != correctpassword):     #limits the number of times a user may enter a password    
    print('please enter a password')        #prompt user to enter password
    password = input()                      #user enters a password

    if password != correctpassword:         #notify the user that their entry was incorrect
        print('Invalid entry.')

    if passwordentries < x:                 #prompt user to try again
        print('please try again')

    if passwordentries == x-1:              #prompt user that the limit is approaching
        print('This is your last attempt before close out')
        print('due to too many incorrect entries')

    passwordentries = passwordentries + 1   #counts number of attempts

    if (password != correctpassword and passwordentries == x+1): #reached user entry limit
        print('too many wrong attempts')
        print('you type like a cat on a keyboard or a crook without a sticky note')
        print('shutting down')              #terminate from too many entries
        break

    if password == correctpassword:         #correct password
        print('Access granted')
        print('Done.')
        break

exit()                                      #terminates program 
        
