# Создать программу-калькулятор в виде класса и несколько методов, как минимум сложение,
# вычитание, деление, умножение, возведение в степень и извлечение квадратного корня.
# Обернуть каждый метод в блок try/except и сделать обработку нескольких исключений, как минимум деление на 0.
# Создать своё исключение, к примеру возведение в отрицательную степень.
class NegativeExponentError(Exception):
    pass


class MyCalc():

    @staticmethod
    def power(a, b):
        if b < 0:
            raise NegativeExponentError('Exponent cannot be negative')
        return a ** b

    @staticmethod
    def sqrt(x):
        if x < 0:
            raise ValueError('Cannot compute square root of negative number')
        return x ** 0.5

    def sum(self, a, b):
        res = 0
        try:
            res = a + b
        except TypeError:
            print('Type Error!')
        return res

    def sub(self, a, b):
        res = 0
        try:
            res = a - b
        except TypeError:
            print('Type Error!')
        return res

    def mult(self, a, b):
        res = 0
        try:
            res = a * b
        except TypeError:
            print('Type Error!')
        except Exception as err:
            print(f'SOMETHING WRONG - {err}!')
        return res

    def rem(self, a, b):
        res = 0
        try:
            res = a / b
        except ZeroDivisionError as err:
            print(f'b is zero - {err}')
        except TypeError:
            print('Type Error!')
        except Exception as err:
            print(f'SOMETHING WRONG - {err}!')
        return int(res)

    def expo(self, a, b):
        res = 0
        try:
            res = a ** b
        except NegativeExponentError as err:
            print(err)
        except Exception as err:
            print(f'SOMETHING WRONG - {err}!')
        return res


cal = MyCalc()
inp_1 = int(input(' Please enter first number: '))
inp_2 = int(input(' Please enter second number: '))
print(cal.sum(inp_1, inp_2))
print(cal.sub(inp_1, inp_2))
print(cal.mult(inp_1, inp_2))
print(cal.rem(inp_1, inp_2))
print(cal.expo(inp_1, inp_2))
print(cal.sqrt(inp_1))
