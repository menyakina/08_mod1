from emp_csv import file_open, insert, save, show_rows
from builtins import print

FILENAME = "new1.csv"

MENU = {
    '1': 'Открыть файл',
    '2': 'Добавить',
    '3': 'Удалить',
    '4': 'Найти по значению',
    '5': 'Сохранить в файл',
    '6': 'Вывести записи',
    '0': '<-Меню',
    'exit': 'Выход'
}

for key, val in MENU.items():
    print(key, '-', val)

while True:
    action = input('>_ ')
    if action == '1':
        file_open()
    elif action == '2':
        print(insert(input('vin_номер: '), input('гос_номер: '), input('марка: '), input('модель: '),
                     int(input('год выпуска: ')), int(input('мощность двигателя: ')),
                     input('пробег: '), int(input('количество владельцев: ')), int(input('стоимость: '))))
    elif action == '5':
        save()
    elif action == '6':
        show_rows()
    elif action == '0':
        for key, val in MENU.items():
            print(key, '-', val)
    elif action == 'exit':
        break
