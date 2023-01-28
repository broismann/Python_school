# Прочитать сохранённый json-файл из задания №18 и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.
import csv
import json

with open('witcher.json') as file:
    loaded_data = json.load(file)

print(loaded_data)

fields_name = ['ID', 'Name', 'Age', 'Cell']

with open('witcher.csv', mode='w', encoding='utf-8') as new_file:
    file_writer = csv.writer(new_file)
    file_writer.writerow(fields_name)
    for number, (key, value) in enumerate(loaded_data.items()):
        cell = ['068000000', '095111111', '066222222', '050333333', '093444444', '063555555', '073666666']
        file_writer.writerow([key, value[0], value[1], cell[number]])
