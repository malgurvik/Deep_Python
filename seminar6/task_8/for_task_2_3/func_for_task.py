
from random import randint


def func(start, stop, count):
    num = randint(start, stop)
    i = 0
    while count > i:
        u_num = int(input(f"введите число в диапазоне от {start} до {stop}:>"))
        if u_num > num:
            print('меньше!')
        elif u_num < num:
            print('больше!')
        else:
            print('Угадал!')
            return True
        i += 1
    return False

if __name__ == '__main__':
    print(func(1, 3, 3))