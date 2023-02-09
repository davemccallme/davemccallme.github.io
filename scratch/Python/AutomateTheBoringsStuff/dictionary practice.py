message = 'There once was a man who lived in a shoe'
count = {}   # set variable to a dictionary

for character in message:
    count.setdefault(character,0) #ensures no error for next line
    count[character] = count[character] + 1

print(count)


message = 'There once was a man who lived in a shoe'
count2 = {}   # set variable to a dictionary

for eachCharacter in 'There once was a man who lived in a shoe':
    count2.setdefault(eachCharacter,0) #ensures no error for next line
    count2[eachCharacter] = count2[eachCharacter] + 1

print(count2)
