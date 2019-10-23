# n1 = input('input an integer between -10 to 10 here: ')
# n1 = int(n1)
#
# if n1 < 5:
#     print('The interger you choose less than 5')

def minimum(x, y):
    if x < y:
        return x
    else:
        return y

result = minimum(1, 4)
print(result)

result = minimum(1, 1)
print(result)
