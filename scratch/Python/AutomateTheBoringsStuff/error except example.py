#program demonstrates try & except functions, with return and error messages

print('please enter a number')      #prompt user for entry

num = input()                       #assign num variable to user input
print(num)

def divbynum(divideBY):
    
    try:
        global num                  #calls the "num" global variable in local function
        num = int(num)              #converts string to text
        return num / divideBY       #tries to perform this function
    except:                         #when error occurs execute this function
        print('Error: please enter a number value')


print(divbynum(2))
print(divbynum(0))
print(divbynum(1))
 
