from datetime import datetime


def decor(func):
    def wrapper():
        start_time = datetime.now()
        print(start_time)
        func()
        end_time = datetime.now()
        print(end_time)
    return wrapper


@decor
def func_1():
    a = 2 ** 25
    r = 0
    for i in range(1, a + 1):
        r += a
    print(f"Let's say I wanna check how long python will count r:")


@decor
def func_2():
    b = 2 ** 25
    r = 0
    for i in range(1, b + 1):
        r += b
    print(f"Let's say I wanna check how long python will count r:")


func_1()
print('*' * 70)
func_2()
