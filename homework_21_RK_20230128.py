# Создать родительский класс auto, у которого есть атрибуты:
# brand, age, cоlor, mark и weight.
# А так же методы: move, birthday и stop.
# Методы move и stop выводят сообщение на экран «move» и «stop»,
# а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.

class Auto:
    brand = 'Audi'
    age = 3
    color = 'green'
    mark = 's4'
    weight = 3000

    def __int__(self, brand='Audi', age=3, mark='s4'):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print('Move!')

    def stop(self):
        print('Stop!')

    def birthday(self):
        self.age += 1

