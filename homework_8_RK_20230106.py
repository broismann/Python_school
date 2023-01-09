def counter(numbers):
    for number in set(numbers):
        repeat = numbers.count(number)
        print(f'Number {number} is repeating: {repeat} times!')
    return


num = [1, 231, 2, 35, 5, 23, 17, 23, 9, 71, 23, 2, 1, 35, 5, 5]
counter(num)
