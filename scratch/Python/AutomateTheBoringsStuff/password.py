#walks user through password entry

print('welcome, please enter a password')
for password in range(3):
    password = input()
    if password == 'swordfish':
        print('access granted')
        quit()
    else:
        print('wrong password, please try again')
    print('you entered too many wrong passwords')
    print('terminating program')
