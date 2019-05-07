# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os


def make_folder(*args):
    for name in args:
        try:
            os.mkdir(name)
            print(f'Директория "{name}" создана.')
        except TypeError:
            print(f'ERROR - Неверно задан тип имени директории: {name}')
        except FileExistsError:
            print(f'ERROR - Невозможно создать. Директория уже существует: {name}')
        except PermissionError:
            print(f'ERROR - Не хватает прав доступа на создание директории: {name}')
        except OSError:
            print(f'ERROR - Синтаксическая ошибка в имени директории: {name}')


def delete_folder(*args):
    for name in args:
        try:
            os.rmdir(name)
            print(f'Директория "{name}" удалена.')
        except FileNotFoundError:
            print(f'ERROR - Невозможно удалить. Директория не существует: {name}')
        except PermissionError:
            print(f'ERROR - Не хватает прав доступа на удаление директории: {name}')
        except OSError:
            print(f'ERROR - Невозможно удалить. Директория не пустая: {name}')


# # Задача-2:
# # Напишите скрипт, отображающий папки текущей директории.
def show_folders(path):
    folders = []
    for el in os.listdir(path):
        if os.path.isdir(el):
            folders.append(el)
    return folders


q_folders = 5
template = 'dir_'
folders = [template + str(i) for i in range(1, q_folders)]
#make_folder(*folders)
delete_folder(*folders)
current_path = os.getcwd()
folder_tree = show_folders(current_path)
for el in folder_tree:
    print(el)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

_, current_file = os.path.split(__file__)
backup_file = current_file + '.backup'
try:
    f1 = open(current_file, 'r', encoding='utf-8')
    content = f1.read()
    f1.close()
    try:
        f2 = open(backup_file, 'w', encoding='utf-8')
        f2.write(content)
        f2.close()
    except FileExistsError:
        print(f'ERROR - Файл {backup_file} уже сущесьвует.')
    except FileNotFoundError:
        print(f'ERROR - Невозможно открыть файл {backup_file} на запись.')
    except PermissionError:
        print(f'ERROR - Не хватает прав доступа на запись файла: {backup_file}')
except FileNotFoundError:
    print(f'ERROR - Невозможно открыть файл {current_file}. Файл не существует!')
except PermissionError:
    print(f'ERROR - Не хватает прав доступа на чтение файла: {current_file}')
