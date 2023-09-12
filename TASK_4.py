from ColorLibraryOfLabWork_2 import *

# 4. Напишите программу, демонстрирующую работу try\except\finally


def solution_4():
    while True:
        try:
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '\nВведите своё число :')
            return is_palindrome(abs(int(input())))
        except ValueError:
            print(Style.BRIGHT + Fore.LIGHTRED_EX +
                  '\U0001f353\U0001f353\U0001f353'
                  'Было введено некорректное значение числа. Ожидается корректный ввод.'
                  '\U0001f353\U0001f353\U0001f353')
        finally:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + '\U0001f353\U0001f353\U0001f353'
                                                    'НИКОГДА не забывайте вводить корректные значения в программу. '
                  'Ведь иногда это приводит к жутким последствиям!\U0001f353\U0001f353\U0001f353')


def is_palindrome(number):
    number = int(number)
    new_number, old_number = 0, number
    while number != 0:
        new_number = new_number * 10 + number % 10
        number = number // 10
    if new_number == old_number:
        return True
    else:
        return False


def task_4():
    print('\n' * 100)
    print(Style.BRIGHT + Fore.BLUE + '+------------------------------------------------------------------------------'
                                     '---------+')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX +
          '  УСЛОВИЕ ЗАДАНИЯ 4:',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
          ' Напишите программу, демонстрирующую работу try\\except\\finally .\n'
          '  Была выбрана следующая задача :\n'
          '  определять является ли число палиндромом.')
    print(Style.BRIGHT + Fore.BLUE + '+-----------------------------------------------------------------------------'
                                     '----------+')
    if solution_4():
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nОТВЕТ ЗАДАНИЯ 4:',
              Style.BRIGHT + Fore.RED + 'Заданное вами число ',
              Style.BRIGHT + Fore.LIGHTCYAN_EX + ' \033[4mЯВЛЯЕТСЯ\033[0m ',
              Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'палиндромом.')
    else:
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nОТВЕТ ЗАДАНИЯ 4:',
              Style.BRIGHT + Fore.RED + 'Заданное вами число ',
              Style.BRIGHT + Fore.LIGHTCYAN_EX + ' \033[4mНЕ ЯВЛЯЕТСЯ\033[0m ',
              Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'палиндромом.')
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          '               ЗАДАНИЕ 4 УСПЕШНО ВЫПОЛНЕНО!               ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+------------------------------------------------------------+')
