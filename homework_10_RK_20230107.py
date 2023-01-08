my_list = [24, 'Merry', 7, 'Christmas', '!', 17, True, None]

new_list = list(map(lambda i: str(i) if type(i) == int else i, my_list))

print(my_list)
print(new_list)
