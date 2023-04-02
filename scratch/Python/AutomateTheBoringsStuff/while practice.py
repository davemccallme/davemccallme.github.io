spam = 0
while spam <= 6:
    spam += 1
    if spam == 5:
        print('2nd to last spam = ' + str(spam))
        continue  # continue statement returns to the top of the while
        
    elif spam == 6 :
        break     #break statments proceed to the next line

    else:
        print('hello ' + str(spam))
    
print('done')
