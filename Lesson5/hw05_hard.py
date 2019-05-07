# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import re


print('sys.argv = ', sys.argv)


def print_help():
    print('help - получение справки')
    print('mkdir <dir_name> - создание директории')
    print('ping - тестовый ключ')
    print('cp <file_name> - создает копию указанного файла')
    print('rm <file_name> - удаляет указанный файл (запросить подтверждение операции)')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
    print('ls - отображение полного пути текущей директории')


def make_dir():
    if not dir_name:
        print('Необходимо указать имя директории вторым параметром')
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))
    except PermissionError:
        print('не хватает прав на создание директории')
    except OSError:
        print(f'ошибка в имени директории {dir_path}')


def ping():
    print("pong")


def ls_():
    print('полный путь текущей директории: ' + os.getcwd())


def cp_():
    if not dir_name:
        print('необходимо указать имя копируемого файла')
        return
    if os.name == 'nt':                                                 # OS = Windows
        filename = dir_name.split('\\')[-1]
        try:
            os.system('copy {} copy_{}'.format(dir_name, filename))
            print(f'файл {filename} скопирован')
        except FileNotFoundError:
            print(f'файл {filename} не существует')
        except PermissionError:
            print('не хватает прав на создание копии файла')
    else:                                                               # OS = Unix
        filename = dir_name.split('/')[-1]
        try:
            os.system('cp {} copy_{}'.format(dir_name, filename))
            print(f'файл {filename} скопирован')
        except FileNotFoundError:
            print(f'файл {filename} не существует')
        except PermissionError:
            print('не хватает прав на создание копии файла')


def rm_():
    if not dir_name:
        print('необходимо указать имя удаляемого файла')
        return
    if os.path.exists(dir_name):
        print(f'файл {dir_name} существует и будет удален')
        answer = input('Y - удалить, N - не удалять').lower()
        if answer == 'y':
            try:
                os.remove(dir_name)
                print(f'файл {dir_name} удален')
            except PermissionError:
                print('не хватает прав на удаление файла')
            except OSError:
                print('файл не может быть удален')
    else:
        print(f'файл {dir_name} не существует')


def cd_():
    if not dir_name:
        print('необходимо указать путь')
        return
    if os.name == 'nt':                                                 # OS = Windows
        if re.search('^[A-Z]:', dir_name) is None:
            print('введен относительный путь')
        else:
            print('введен абсолютный путь')
        try:
            os.chdir(dir_name)
            ls_()
        except Exception as error:
            print(error)
    else:                                                               # Unix
        if re.search('^/',dir_name) is None:
            print('относительный путь')
        else:
            print('абсолютный путь')
        try:
            os.chdir(dir_name)
            ls_()
        except Exception as error:
            print(error)


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp_,
    "rm": rm_,
    "cd": cd_,
    "ls": ls_
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print('Задан неверный ключ')
        print('Укажите ключ help для получения справки')
