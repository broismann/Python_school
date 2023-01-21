str_1 = input('Please enter any string 1: ')
str_2 = input('Please enter any string 2: ')
str_3 = input('Please enter any string 3: ')
str_4 = input('Please enter any string 4: ')

with open("two_strings.txt", "w") as f:
    f.write(str_1 + "\n" + str_2 + "\n")

with open("two_strings.txt", "a") as f:
    f.write(str_3 + "\n" + str_4 + "\n")

