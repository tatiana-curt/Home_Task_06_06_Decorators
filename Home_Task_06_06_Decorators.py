# Написать декоратор - логгер. Он записывает в файл:
# - дату и время вызова функции
# - имя функции
# - аргументы, с которыми вызвалась
# - возвращаемое значение.

import hashlib
import datetime
import random

# _________________Задание 1 и 2. Реализация без вложенности. (передача пути в параметре **kwargs) ____________
def log(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        call_time = datetime.datetime.now()
        name_call_function = old_function.__name__
        path_log = list(kwargs.values())[0]

        with open(path_log, 'a', encoding='utf-8') as file:
            file.write(f'Дата и время вызова функции: "{call_time}"\nИмя функции: "{name_call_function}"\n'
                       f'Аргументы: args - {args}; kwargs - {kwargs}\nРезультат: "{result}"\n')
        return result
    return new_function

@log
def md5_generator(path, **kwargs):
    with open(path, 'rb') as file:
        strings = file.readlines()
        for string in strings:
            yield hashlib.md5(string).hexdigest()

for string in md5_generator('wiki_links.txt', path_log = 'C:\\Users\\t.petruk\\dev\\Home_Task_06_06_Decorators\\logs.txt'):
    print(string)




# __________________Пробую декоратор для другой функции_______________
# @log
# def pow(**kwargs):
#     random_list = [random.randrange(1, 100) for _ in range(100)]
#     return random_list
#
# result = pow(path_log = 'C:\\Users\\t.petruk\\dev\\Home_Task_06_06_Decorators\\logs.txt')
# print(result)





# _________________Задание 1 и 2. Реализация с вложенностью_____________________
# def path_log(path):
#     def log(old_function):
#         def new_function(*args, **kwargs):
#             result = old_function(*args, **kwargs)
#             call_time = datetime.datetime.now()
#             name_call_function = old_function.__name__
#
#             with open(path, 'a', encoding='utf-8') as file:
#                 file.write(f'Дата и время вызова функции: "{call_time}"\nИмя функции: "{name_call_function}"\n'
#                            f'Аргументы: args - {args}; kwargs - {kwargs}\nРезультат: "{result}"\n')
#             return result
#         return new_function
#     return log
#
# @path_log('logs_2.txt')
# def md5_generator(path):
#     with open(path, 'rb') as file:
#         strings = file.readlines()
#         for string in strings:
#             yield hashlib.md5(string).hexdigest()
#
# for string in md5_generator('wiki_links.txt'):
#     print(string)