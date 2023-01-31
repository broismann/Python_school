inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']

result = tuple(filter(lambda i: i.lower()[0::] == i.lower()[::-1], inputdata))

print(result)
