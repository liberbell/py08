import calendar
import math
import random

cal = calendar.month(2019,10)
print(cal)

result = math.sqrt(49)
print(result)

number = random.randint(1, 100)
print(number)

for i in range(100):
    number = random.randint(1, 100)
    state1 = 0
    state2 = 0
    state3 = 0
    state4 = 0
    state5 = 0
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

print('1 is: ', state1)
print('2 is: ', state2)
