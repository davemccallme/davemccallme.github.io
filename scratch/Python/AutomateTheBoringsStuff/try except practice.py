#this program tries to divide by 42 and returns error if by 0


def divBy42(divideBy):
    try:
        return 42/divideBy
    except:
        print('Error: Cannot divide by 0')


print(divBy42(5))
print(divBy42(4))
print(divBy42(3))
print(divBy42(2))
print(divBy42(1))
print(divBy42(0))





