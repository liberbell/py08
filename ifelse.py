raining = input('Is it raining yes/no: ')
unbrella = input('Do you have an unbrella yes/no: ')

if raining == 'yes' and unbrella == 'yes':
    print('Don`t forget your unbrella when you go out.')
elif raining == 'yes' and unbrella == 'no':
    print('Wear a waterproof jacket when yuo go out.')

x = input('Enter a number here: ')
x = float(x)
if x < 2:
    print('The number is less than two.')
elif x < 6:
    print('The number is less than six.')
elif x < 8:
    print('The number is less than eight.')
elif x < 10:
    print('The number is less than ten.')

x = 1
print(float(x))
