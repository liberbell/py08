def greeting():
    print('Hey there!')

greeting()

def greet(name):
    print('Hi ' + name + '!')

greet('Josh')

def aquire(x):
    return x * x

result = aquire(5)
print(result)

anotherOne = aquire(result)
print(anotherOne)

def sumofSquares(x, y):
    square1 = x * x
    square2 = y * y
    return square1 + square2

result = sumofSquares(2, 3)
print(result)

def is_it_raining():
    raining = input('Is it raining today?')
    return raining

monday_raining = is_it_raining()
