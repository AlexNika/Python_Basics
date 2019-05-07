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
        if os.path.isfile(name):
            print(f'Невозможно удалить такую директорию, т.к. {name} - это файл')
        else:
            try:
                os.rmdir(name)
                print(f'Директория "{name}" удалена.')
            except FileNotFoundError:
                print(f'ERROR - Невозможно удалить. Директория не существует: {name}')
            except PermissionError:
                print(f'ERROR - Не хватает прав доступа на удаление директории: {name}')
            except OSError:
                print(f'ERROR - Невозможно удалить. Директория не пустая: {name}')


def show_folders(path):
    folders = []
    files = []
    for el in os.listdir(path):
        if os.path.isdir(el):
            folders.append(el)
        elif os.path.isfile(el):
            files.append(el)
    return folders, files


def change_folder(path):
    try:
        os.chdir(path)
        print('Вы успешно перешли в директорию.')
        print(f'Текущая директория - {os.getcwd()}')
    except FileNotFoundError:
        print(f'ERROR - Невозможно перейти. Такой директория не существует: {path}')
    except OSError:
        print(f'ERROR - Синтаксическая ошибка в имени директории: {path}')
