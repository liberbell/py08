import calendar
import math
import random

cal = calendar.month(2019,10)
print(cal)

result = math.sqrt(49)
print(result)

number = random.randint(1, 100)
# print(number)
state1 = 0
state2 = 0
state3 = 0
state4 = 0
state5 = 0
for i in range(1000):
    number = random.randint(1, 5)
    # print(number)
    if number == 1:
        state1 += 1
    elif number == 2:
        state2 += 1
    elif number == 3:
        state3 += 1
    elif number == 4:
        state4 += 1
    else:
        state5 +=1
    # print(number)

print('1 is: ', state1)
print('2 is: ', state2)
print('3 is: ', state3)
print('4 is: ', state4)
print('5 is: ', state5)
