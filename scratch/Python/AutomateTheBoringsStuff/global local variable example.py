#defines and demonstrates local and global variables within functions

spam = 24               #the "global variable" spam

print(spam)             #show global spam

def spam():             #the "function" spam defined
    spam = 36           #local spam value
    print(spam)         #calls local spam
    bacon()             #calls bacon function below
    print(spam)
    
def bacon():            #the "function" bacon defined
    spam = 42           #the "local variable" spam
    ham = 101
    print("test")       #demonstrates various wasys to write out ''\'')
    print('test')
    print("doesn't")
    print('doesn\'t') 
    print(spam)         #show user local spam value

spam()                  #calls the spam function
print("Done program 1") #displays the 2 functions







#functions without assigned local variables will look globally for variables
#that match the call, but not the other way around (global looking in a local )

print(' start prorgam 2')
def spam():
    print(eggs)             #program looks globally for "eggs" variable

eggs = 42
spam()                      #calls spam "function"
print('done program 2')


print('start program 3')

def spam():
    global eggs             #tells the function to refer to global "eggs"
    eggs = "Hello"          #and reassigns the global to this local value
    print(eggs)

eggs = 42                   #global assignment
print(eggs)                 #print global "eggs"
spam()                      #print reassigned "eggs" from spam function
print(eggs)
