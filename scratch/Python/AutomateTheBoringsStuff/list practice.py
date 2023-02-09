x= 6                             #low limit integer
y = 20                           #high limit integer
z = 1                           #number of steps (integer)
lucifer = 666

spam = list(range(x,y,z))        #creates a list[] with range ( x,y ) and z steps
spam = list(range(x+1,y+1,z+1))  #swap current list with new "list + 1"

spam[6] = lucifer                #modify the list at [1]

for i in range(len(spam)):       #creates loop equal to length of list spam
	print(str(spam[i]) + ' is ' + str(i) + ' in the list') # prints coordinates of list spam


a = 'aaa'
b = 'bbb'

print(a)
print(b)

a = b 
b = a  #a is now b so we should see 'bbb'

print(a)
print(b)
