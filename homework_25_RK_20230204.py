class Person():
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    def introduce(self):
        return f'Hi, I am {self.name} and I am {self.age} years old.'

    @classmethod
    def total_population(cls):
        return cls.population

    @staticmethod
    def is_adult(age):
        return age >= 18

    def __str__(self):
        return f'Person(name="{self.name}", age={self.age})'


person1 = Person('Alice', 25)
person2 = Person('Bob', 32)

print(person1.introduce())
print(person2.introduce())

print('Total population:', Person.total_population())

print('Is Alice an adult?', Person.is_adult(person1.age))
print('Is Bob an adult?', Person.is_adult(person2.age))

print(person1)
