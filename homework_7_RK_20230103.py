old_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60, 'g': 70}

new_dict = {value: key for key, value in old_dict.items()}

print(new_dict)
