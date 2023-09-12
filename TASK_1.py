from ColorLibraryOfLabWork_2 import *
from math import sqrt

# 1. Написать функцию triangle, принимающую 1 аргумент — сторону равностороннего треугольника,
# и возвращающую 2 значения
# (с помощью кортежа): периметр и площадь треугольника. – 2 балла


def triangle(side):
    answer = (-1, -1)
    try:
        answer = (round(float(side) * 3, 3), round(float(side) ** 2 * sqrt(3) / 4, 3))
        return answer
    except ValueError:
        print(Style.BRIGHT + Fore.LIGHTRED_EX + '\U0001f353\U0001f353\U0001f353'
                                                'Введено некорректное значение стороны. Ожидается корректный ввод. '
              'Учтите, что сторона треугольника есть число!\U0001f353\U0001f353\U0001f353')
        return answer


def solution_1():
    while True:
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + 'Введите значение стороны треугольника : ')
        perimetr, square = triangle(input())
        if perimetr > 0:
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nОТВЕТ ЗАДАНИЯ 1:',
                  Style.BRIGHT + Fore.RED + 'Периметр треугольника равен',
                  Style.BRIGHT + Fore.LIGHTCYAN_EX + f'\033[4m{perimetr}\033[0m',
                  Style.BRIGHT + Fore.RED + ', а его площадь равна',
                  Style.BRIGHT + Fore.LIGHTCYAN_EX + f' \033[4m{square}.\033[0m')
            break
        else:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + '\U0001f353\U0001f353\U0001f353'
                                                    'Сторона треугольника не может быть отрицательной и нулем!'
                                                    '\U0001f353\U0001f353\U0001f353')


def task_1():
    print('\n' * 100)
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------------------------'
                                     '--------------------------------------------+')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX +
          '  УСЛОВИЕ ЗАДАНИЯ 1:',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
          ' Написать функцию triangle, принимающую 1 аргумент — сторону равностороннего треугольника,\n '
          ' и возвращающую 2 значения (с помощью кортежа): периметр и площадь треугольника.',
          )
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------------------------'
                                     '--------------------------------------------+')
    solution_1()
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          '               ЗАДАНИЕ 1 УСПЕШНО ВЫПОЛНЕНО!               ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+------------------------------------------------------------+')
