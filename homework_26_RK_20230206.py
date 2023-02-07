# Создать программу-калькулятор в виде класса и несколько методов, как минимум сложение,
# вычитание, деление, умножение, возведение в степень и извлечение квадратного корня.
# Обернуть каждый метод в блок try/except и сделать обработку нескольких исключений, как минимум деление на 0.
# Создать своё исключение, к примеру возведение в отрицательную степень.
class NegativeExponentError(Exception):
    pass


class MyCalc():

    @staticmethod
    def power(a, b):
        try:
            if b < 0:
                raise NegativeExponentError('Exponent cannot be negative')
            res = a ** b
            return res
        except NegativeExponentError as err:
            print(f'NegativeExponentError: {err} ')
        return None

    @staticmethod
    def sqrt(a):
        try:
            if a < 0:
                raise ValueError('Cannot compute square root of negative number')
            res = a ** 0.5
            return res
        except Exception as err:
            print(f'An error occurred: {err}!')
            return None

    def sum(self, a, b):
        try:
            res = a + b
            return res
        except ValueError as err:
            print(f'Type Error: {err}')
        except Exception as err:
            print(f'Value Error: {err}')
        return None

    def sub(self, a, b):
        try:
            res = a - b
            return res
        except ValueError as err:
            print(f'Type Error: {err}')
        except Exception as err:
            print(f'Value Error: {err}')
        return None

    def mult(self, a, b):
        try:
            res = a * b
            return res
        except ValueError as err:
            print(f'Type Error: {err}')
        except Exception as err:
            print(f'SOMETHING WRONG - {err}!')
        return None

    def rem(self, a, b):
        try:
            if b == 0:
                raise ZeroDivisionError('Cannot divide by zero!')
            res = a / b
            return int(res)
        except ZeroDivisionError as err:
            print(f'b is zero - {err}')
        except TypeError as err:
            print(f'Type Error: {err}')
        except Exception as err:
            print(f'SOMETHING WRONG - {err}!')
        return None



cal = MyCalc()
try:
    inp_1 = int(input('Please enter first number: '))
    inp_2 = int(input('Please enter second number: '))
except ValueError:
    print('Invalid input, only numbers are allowed!')
    inp_1 = int(input('Please enter first number: '))
    inp_2 = int(input('Please enter second number: '))
print(cal.sum(inp_1, inp_2))
print(cal.sub(inp_1, inp_2))
print(cal.mult(inp_1, inp_2))
print(cal.rem(inp_1, inp_2))
print(cal.power(inp_1, inp_2))
print(cal.sqrt(inp_1))
