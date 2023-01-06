your_number = int(input('Please enter your number: '))
result = lambda your_number: print("This is even!") if your_number % 2 == 0 else print('This is an odd!')
result(your_number)
