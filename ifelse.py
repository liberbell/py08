# raining = input('Is it raining yes/no: ')
# unbrella = input('Do you have an unbrella yes/no: ')
#
# if raining == 'yes' and unbrella == 'yes':
#     print('Don`t forget your unbrella when you go out.')
# elif raining == 'yes' and unbrella == 'no':
#     print('Wear a waterproof jacket when yuo go out.')
#
# x = input('Enter a number here: ')
# x = float(x)
# if x < 2:
#     print('The number is less than two.')
# elif x < 6:
#     print('The number is less than six.')
# elif x < 8:
#     print('The number is less than eight.')
# elif x < 10:
#     print('The number is less than ten.')
#
# x = 1
# print(float(x))
# x = 1.5
# print(int(x))

x = input('Enter a number here: ')
x = float(x)
if x < 2:
    print('The number is less than two.')
if x < 6:
    print('The number is less than six.')
if x < 8:
    print('The number is less than eight.')
if x < 10:
    print('The number is less than ten.')

def abs_val(num):
    if num < 0:
        return -1 * num
    elif num == 0:
        return 0
    else:
        return num

result = abs_val(5.4)
print(result)
result = abs_val(0)
print(result)
result = abs_val(-100)
print(result)
