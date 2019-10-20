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

result = sumofSquares(10, 20)
print(result)
