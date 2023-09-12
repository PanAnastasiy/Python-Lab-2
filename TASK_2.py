from ColorLibraryOfLabWork_2 import *


# 2. Напишите функцию, которая будет принимать один аргумент.
# Если в функцию передаётся список, найти сумму после второго отрицательного элемента.
# Вывести на экран все четные числа.
# Если множество, найти максимальный и минимальный элементы.
# Число – вывести все простые числа до заданного.
# Строка – вывести все цифры отдельным списком.
# Сделать проверку со всеми этими случаями. – 4 балла


def solution_2():
    while True:
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\n\nВведите ваш аргумент функции для решения задания 2 : ')
        argument = input()
        if argument.isdigit():
            argument = int(argument)
        elif argument[0] == '{' and argument[-1] == '}':
            try:
                argument = set([int(i) for i in argument[1:-1].split(',')])
            except ValueError:
                print(Style.BRIGHT + Fore.LIGHTRED_EX +
                      '\n\n\U0001f353\U0001f353\U0001f353'
                      'Множество должно содержать только целые числа и не должно быть пустым!'
                      '\U0001f353\U0001f353\U0001f353')
                continue
        elif argument[0] == '[' and argument[-1] == ']':
            try:
                argument = [int(i) for i in argument[1:-1].split(',')]
            except ValueError:
                print(Style.BRIGHT + Fore.LIGHTRED_EX +
                      '\n\n\U0001f353\U0001f353\U0001f353'
                      'Список должен содержать только целые числа и не должен быть пустым!'
                      '\U0001f353\U0001f353\U0001f353')
                continue
        func_of_task_2(argument)
        break


def func_of_task_2(arg):
    if isinstance(arg, list):
        print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '\nВами был введён',
              Style.BRIGHT + Fore.LIGHTRED_EX + '\033[4mСПИСОК.\033[0m')
        if min(arg) >= 0:
            print(Style.BRIGHT + Fore.LIGHTRED_EX +
                  '\n\U0001f353\U0001f353\U0001f353'
                  'В введённом вами списке нет отрицательных элементов! Какие-либо действия производится не будут.'
                  '\U0001f353\U0001f353\U0001f353')
        elif len([i for i in arg if i < 0]) == 1:
            print(Style.BRIGHT + Fore.LIGHTRED_EX +
                  '\n\U0001f353\U0001f353\U0001f353'
                  'В введённом вами списке ОДИН отрицательный элемент! Какие-либо действия производится не будут.'
                  '\U0001f353\U0001f353\U0001f353')
        elif index_of_second_negative(arg) == len(arg) - 1:
            print(Style.BRIGHT + Fore.LIGHTRED_EX +
                  '\n\U0001f353\U0001f353\U0001f353'
                  'В введённом вами списке второй отрицательный элемент находится в самом конце списка!'
                  ' Какие-либо действия производится не будут.'
                  '\U0001f353\U0001f353\U0001f353')
        else:
            count, j = 0, index_of_second_negative(arg)
            for i in range(j + 1, len(arg)):
                count += arg[i]
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX +
                  '\nСумма элементов после ВТОРОГО отрицательного элемента равна : ', count)
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + 'Второй отрицательный элемент :', arg[j])
    elif isinstance(arg, set):
        print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '\nВами было введёно',
              Style.BRIGHT + Fore.LIGHTRED_EX + '\033[4mМНОЖЕСТВО.\033[0m')
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nОТВЕТ ЗАДАНИЯ 2: ',
              Style.BRIGHT + Fore.LIGHTGREEN_EX +
              f'Максимальный элемент множества : {max(arg)}, минимальный элемент множества : {min(arg)}.')
    elif isinstance(arg, int):
        print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '\nВами было введёно',
              Style.BRIGHT + Fore.LIGHTRED_EX + '\033[4mЧИСЛО.\033[0m')
        lst = [i for i in range(2, arg + 1) if is_prime(i)]
        print_answer_int(lst)
    elif isinstance(arg, str):
        print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '\nВами была введёна',
              Style.BRIGHT + Fore.LIGHTRED_EX + '\033[4mСТРОКА.\033[0m')
        lst = list(set([i for i in arg if i.isdigit()]))
        print_answer_str(lst)


def index_of_second_negative(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] < 0:
            count += 1
        if count == 2:
            return i


def print_answer_int(lst):
    if lst:
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nОТВЕТ ЗАДАНИЯ 2: ',
              Style.BRIGHT + Fore.LIGHTGREEN_EX +
              f'Все простые числа до заданного вами числа : ', *lst)
    else:
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nОТВЕТ ЗАДАНИЯ 2: ',
              Style.BRIGHT + Fore.LIGHTRED_EX +
              '\U0001f353\U0001f353\U0001f353Увы простые числа отсутствуют перед вашим числом.'
              '\U0001f353\U0001f353\U0001f353')


def print_answer_str(lst):
    if lst:
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nОТВЕТ ЗАДАНИЯ 2: ',
              Style.BRIGHT + Fore.LIGHTGREEN_EX +
              f'Все встречающиеся цифры в строке представлены в виде списка : ', *lst)
    else:
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nОТВЕТ ЗАДАНИЯ 2: ',
              Style.BRIGHT + Fore.LIGHTRED_EX +
              '\U0001f353\U0001f353\U0001f353Увы но в заданной строке отсутствуют цифры.'
              '\U0001f353\U0001f353\U0001f353')


def is_prime(number):
    for j in range(2, int(number ** 0.5) + 1):
        if number % j == 0:
            return False
    return True


def task_2():
    print('\n' * 100)
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------------------------'
                                     '--------------------------------------------+')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX +
          '  УСЛОВИЕ ЗАДАНИЯ 2:',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
          '  Напишите функцию, которая будет принимать один аргумент.\n '
          ' Если в функцию передаётся список, найти сумму после второго отрицательного элемента.\n'
          '  Вывести на экран все четные числа.\n'
          '  Если множество, найти максимальный и минимальный элементы.\n'
          '  Число – вывести все простые числа до заданного.\n'
          '  Строка – вывести все цифры отдельным списком.\n'
          '  Сделать проверку со всеми этими случаями.'
          )
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------------------------'
                                     '--------------------------------------------+')
    solution_2()
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          '               ЗАДАНИЕ 2 УСПЕШНО ВЫПОЛНЕНО!               ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+------------------------------------------------------------+')
