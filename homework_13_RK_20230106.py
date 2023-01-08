import random


def divining(a, b):
    print(f'your number is {a}; {b} is mine')
    if a != b:
        print(f'Sorry, you lose:(')
    else:
        print('Congrats! You von!')


number = int(input('Can you try to divine my number, please enter any between 0 and 10: '))
my_num = random.randint(1, 10)
divining(number, my_num)
