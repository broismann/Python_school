n = input('Please enter any integer: ')
result = 0
counter = 0

while counter <= int(n):
    counter += 1
    print(counter)
    if not n.isdigit() or int(n) <= 0:
        print('Man, it is wrong input, please try again')
        continue
    elif counter % 3 != 0:
        result += counter ** 3
        print(f'Result: {result}')
    else:
        print(f'skipped {counter}')


