def counter(numbers):
    for number in numbers:
        repeat = numbers.count(number)
        print(f'Number {number} is repeating: {repeat} times!')
    return

num = [1, 23, 2, 35, 5, 23, 17, 23, 9, 71, 23, 2, 1, 35, 5]
counter(num)