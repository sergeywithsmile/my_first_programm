import csv  # подключение библиотеки csv для работы с файлами формата CSV
import sys  # обеспечивает доступ к функии закрытия программы sys.exit()
from mylist import DoubleList

print('Вас приветствует программа для работы с файлами формата .CSV')  # приветствие

# path_to_the_file_1 = input('Введите путь к файлу и его название\n'
#                            '(Пример: D:\data_about_users_new.csv): ')  # переменная, содержащая путь к файлу
path_to_the_file_1 = 'D:\Python\Serg\data_users.txt'
my_list = DoubleList()

while True:
    my_list.load_from_file(path_to_the_file_1)
    selection_8 = int(input('Вывод чисел: введите 1\n'
                            'Изменение чисел: введите 2\n'
                            'Для выхода из программы:  введите 0\n'))  # переменной selection_8 присваивается целочисленное значение
    if selection_8 == 1:  # условие вывода данных о пользователях
        my_list.print()

    elif selection_8 == 2:   # условие изменения информации о пользователях
        selection_9 = int(input('Удаление чисел: введите 1\n'
                                'Добавление чисел: введите 2\n'
                                'Добавление чисел по индексу: введите 3\n'))
        if selection_9 == 1:
            my_list.print()
            selection_2 = int(input(
                'Сколько чисел удалить? '))  # переменной selection_2 присваивается целочисленное значение(int) - количество пользователей для удаление
            i = 0
            count_deleted_number = 0
            while i < selection_2:  # цикл, при котором будет удаляться информация о пользователях. Столько, сколько было присвоено переменной selection_2
                selection_3 = int(input(
                    'Удалить число: '))  # переменной selection_3 присваивается целое число, соответствующее порядковому номеру пользователя в списке
                try:
                    my_list.delete(my_list.search(selection_3))  # функция del  удаляет элемент списка csv_reader_list
                    count_deleted_number = count_deleted_number + 1
                except Exception:
                    print("Ошибка удаления")
                    i = i + 1
                    continue
                my_list.print()
                print(f'Вы удалили число {selection_3}.')
                i = i + 1
            else:
                print(f'Вы удалили {count_deleted_number} чисел.')
                my_list.print()
            path_to_the_file_2 = input('Введите название файла и путь для его сохранения\n'
                                       '(Пример: D:\data_about_users_new.txt):  ')
            my_list.save_in_file(path_to_the_file_2)
        elif selection_9 == 2:
            my_list.print()
            selection_1 = int(input('Сколько чисел ввести: '))
            i = 0
            while i < selection_1:
                new_num = input('Введите число: ')  # присваивание переменной new_names значения, вводимое пользователем
                my_list.insert(new_num)  # добавление списка new_users  в конец списка csv_reader_lest
                i = i + 1
                my_list.print()
            else:
                print(f'Вы ввели {selection_1} чисел.')
            path_to_the_file_2 = input('Введите путь сохранения файла и его название\n'
                                       '(В таком формате: D:\data_about_users_new.txt): ')
            my_list.save_in_file(path_to_the_file_2)
            print(f'Файл сохранён в {path_to_the_file_2}.')
        elif selection_9 == 3:
            my_list.print()
            selection_4 = int(input('Скольким чисел ввести по индексу: '))
            i = 0
            while i < selection_4:  # пока selection_4 будет меньше i = 0 будут выполняться условия ниже
                selection_5 = int(input('Какое число вставить: '))
                selection_7 = int(input('Каким индекс: '))
                my_list.insert_by_index(selection_5, selection_7)
                i = i + 1
            else:
                print(f'Вы заменили {i} чисел.')
                my_list.print()
            path_to_the_file_3 = input('Введите путь для сохранения файла и его название\n'
                                       '(В таком формате: D:\data_about_users.txt): ')
            my_list.save_in_file(path_to_the_file_3)

        else:
            path_to_the_file_3 = input('Введите путь сохранения файла и его название\n'
                                       '(В таком формате: D:\data_about_users_new.txt): ')

            my_list.save_in_file(path_to_the_file_3)
            print(f'Файл сохранён в {path_to_the_file_3}.')
        input('Нажмите ENTER для выхода в главное меню.')
    elif selection_8 == 0:  # функция выхода из программы
        sys.exit()