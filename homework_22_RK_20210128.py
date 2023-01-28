class Auto():
    color = None
    weight = None

    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print('Move!')

    def stop(self):
        print('Stop!')

    def birthday(self):
        self.age += 1

class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print('Attention!')
        super().move()

    def load(self):
        import time
        time.sleep(1)
        print('Loading...')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        print('Attention!')
        super().move()
        print(f'max speed is {self.max_speed}')

#Перевіряємо

truck_1 = Truck('Ford', 3, 'Transit', 15000)
truck_2 = Truck('Renault', 5, 'Doblo', 20000, color='blue', weight=7000)
print(truck_1.brand)
print(truck_1.age)
print(truck_1.mark)
print(truck_1.color)
print(truck_1.weight)
print(truck_1.max_load)
truck_1.move()
truck_1.load()
print('_'* 100)
print(truck_2.brand)
print(truck_2.age)
print(truck_2.mark)
print(truck_2.color)
print(truck_2.weight)
print(truck_2.max_load)
truck_2.move()
truck_2.load()
print('#'* 100)
car_1 = Car('Toyota', 11, 'Prius', 220, 'Black')
car_2 = Car('Tesla', 1, 'Model3', 290)
print(car_1.brand)
print(car_1.age)
print(car_1.mark)
print(car_1.color)
print(car_1.weight)
print(car_1.max_speed)
car_1.move()
print('_'* 100)
print(car_2.brand)
print(car_2.age)
print(car_2.mark)
print(car_2.color)
print(car_2.weight)
print(car_2.max_speed)
car_2.move()

