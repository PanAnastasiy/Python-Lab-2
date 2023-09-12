from ColorLibraryOfLabWork_2 import *
from random import *

# 3. Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
# Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j. – 2 балла


def solution_3():
    n, m, matrix = initialization_matrix()
    i, j = column_selection(m)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '\nДО изменений матрица имеет следующий вид :\n')
    print_matrix(matrix, n, m, i, j)
    for t in range(n):
        matrix[t][i - 1], matrix[t][j - 1] = matrix[t][j - 1], matrix[t][i - 1]
    i, j = j, i
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '\nПОСЛЕ изменений матрица имеет следующий вид :\n')
    print_matrix(matrix, n, m, i, j)
    print_color_of_columns()


def print_color_of_columns():
    print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\n\U0001f353Красный',
          Style.BRIGHT + Fore.LIGHTWHITE_EX + ' - цвет ',
          Style.BRIGHT + Fore.LIGHTRED_EX + '1-ого',
          Style.BRIGHT + Fore.LIGHTWHITE_EX + ' выбранного вами столбца.')
    print(Style.BRIGHT + Fore.LIGHTBLUE_EX + '\n  Синий',
          Style.BRIGHT + Fore.LIGHTWHITE_EX + ' - цвет ',
          Style.BRIGHT + Fore.LIGHTBLUE_EX + '2-ого',
          Style.BRIGHT + Fore.LIGHTWHITE_EX + ' выбранного вами столбца.')


def initialization_matrix():
    while True:
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\n\nВведите количество строк и столбцов матрицы через пробел : ')
        rows, columns = [int(i) for i in input().split()]
        if columns <= 0 or rows <= 0:
            print(Style.BRIGHT + Fore.LIGHTRED_EX +
                  '\n\U0001f353\U0001f353\U0001f353'
                  'Недопустимые значения для столбцов и строк матрицы. Задача не выполнима. Повторите ввод!'
                  '\U0001f353\U0001f353\U0001f353')
        elif columns == 1:
            print(Style.BRIGHT + Fore.LIGHTRED_EX +
                  '\n\U0001f353\U0001f353\U0001f353Матрица имеет один столбец. Задача не выполнима. Повторите ввод!'
                  '\U0001f353\U0001f353\U0001f353')
        else:
            break
    array = [[randint(-25, 25) for _ in range(int(columns))] for _ in range(int(rows))]
    return rows, columns, array


def column_selection(columns):
    while True:
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\nВведите номер 1-ого столбца, который желаете сменить :')
        first_column = input()
        if first_column.isdigit():
            first_column = int(first_column)
            if first_column > columns or first_column < 1:
                print(Style.BRIGHT + Fore.LIGHTRED_EX +
                      '\n\U0001f353\U0001f353\U0001f353'
                      'Заданный вами столбец отсутствует в матрице. Учтите размерности матрицы!'
                      '\U0001f353\U0001f353\U0001f353')
            else:
                break
        else:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                    'Номер столбца есть число целое и положительное!'
                                                    '\U0001f353\U0001f353\U0001f353')
    while True:
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\nВведите номер 2-ого столбца, который желаете сменить :')
        second_column = input()
        if second_column.isdigit():
            second_column = int(second_column)
            if (second_column > columns or second_column < 1) or second_column == first_column:
                print(Style.BRIGHT + Fore.LIGHTRED_EX +
                      '\n\U0001f353\U0001f353\U0001f353'
                      'Заданный вами столбец отсутствует в матрице или равен первому столбцу.'
                      ' Учтите размерности матрицы!\U0001f353\U0001f353\U0001f353')
            else:
                break
        else:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + '\n\U0001f353\U0001f353\U0001f353'
                                                    'Номер столбца есть число целое и положительное!'
                                                    '\U0001f353\U0001f353\U0001f353')
    return first_column, second_column


def print_matrix(array, rows, columns, first_column, second_column):
    for t in range(rows):
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '(  ', end='')
        for k in range(columns):
            if k + 1 == first_column:
                print(Style.BRIGHT + Fore.LIGHTRED_EX + str(array[t][k]).ljust(5), end='')
            elif k + 1 == second_column:
                print(Style.BRIGHT + Fore.LIGHTBLUE_EX + str(array[t][k]).ljust(5), end='')
            else:
                print(str(array[t][k]).ljust(5), end='')
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + ')\n', end='')


def task_3():
    print('\n' * 100)
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------------------------'
                                     '------------------------+')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX +
          '  УСЛОВИЕ ЗАДАНИЯ 3:',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
          'Дан двумерный массив и два числа: i и j.\n  '
          'Поменяйте в массиве столбцы с номерами i и j и выведите результат.\n  '
          'Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j. '
          )
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------------------------'
                                     '------------------------+')
    while True:
        try:
            solution_3()
            break
        except ValueError:
            print(Style.BRIGHT + Fore.RED +
                  '\n\n\U0001f353\U0001f353\U0001f353Учтите, что количество строк и столбцов,'
                  ' то есть переменные n и m могут быть только целыми положительными числами! '
                  'Повторите ввод переменных!\U0001f353\U0001f353\U0001f353')
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          '               ЗАДАНИЕ 3 УСПЕШНО ВЫПОЛНЕНО!               ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+------------------------------------------------------------+')
