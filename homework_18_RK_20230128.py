# Созадать словарь в качестве ключа которого будет 6-ти значное число,
# а в качестве значений кортеж состоящий из 2-х элементов – имя(str), возраст(int).
# Сделать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл.
import json
my_dict = {
    100000: ('Geralt', 57),
    200000: ('Jennefer', 99),
    300000: ('Cirilla', 20),
    400000: ('Emhyr var Emreis ', 51),
    500000: ('Vesemir', 333),
    600000: ('Gaunter O-Dimm', 4092),
    700000: ('Olgerd von Everec', 81)
}
print(my_dict)

with open('witcher.json', 'w') as file:
    json.dump(my_dict, file)
