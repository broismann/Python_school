while True:
    n = input('Please enter any integer: ')
    result = 0
    if not n.isdigit() or int(n) <= 0:
        print('Man, it is wrong input, please try again')
        continue

    for i in range(1, int(n)+1):
        if i % 3 != 0:
            result += i ** 3
        print(i, result)
    break







