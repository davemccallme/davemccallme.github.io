print('please enter a name...')
name = input()
print('please enter an age')
age = input()

if name == 'Alice':
    print('hi Alice')
elif age < 20:
    print('get outta here kiddo')
elif age >100:
    print('you''' 're quite the granny')
elif name == 'Bob':
    print('Welcome Bob')
elif name != 'Bob':
    print('game over')
quit()
