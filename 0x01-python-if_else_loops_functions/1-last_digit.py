#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    mod = number % 10
elif number < 0:
    mod = number % -10
if mod > 5:
    print('Last digit of ' + str(number) + ' is ' + str(mod) + ' and is greater than 5')
elif mod == 0:
    print('Last digit of ' + str(number) + ' is ' + str(mod) + ' and is 0')
elif mod < 6 and not 0:
    print('Last digit of ' + str(number) + ' is ' + str(mod) + ' and is less than 6 and not 0')
