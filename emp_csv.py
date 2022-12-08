import csv

csv_file = []


# открыть файл
def file_open():
    global csv_file
    with open('new1.csv', "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            csv_file.append(row)
    print('Файл открыт. Записей:', len(csv_file))


def insert(vin, number, marka, model, year_v, power, probeg, kol, cost):
    try:
        global csv_file
        csv_file.append({'vin_номер': vin,
                         'гос_номер': number,
                         'марка': marka,
                         'модель': model,
                         'год выпуска': year_v,
                         'мощность двигателя': power,
                         'пробег': probeg,
                         'количество владельцев': kol,
                         'стоимость': cost})
    except Exception as e:
        return f"Ошибка при добавлении новой записи {e}"
    print("Данные добавлены")


def save():
    with open('new1.csv', "w", encoding="utf-8", newline="") as file:
        columns = ("vin_номер", "гос_номер", "марка", "модель", "год выпуска", "мощность двигателя", "пробег",
                   "количество владельцев", "стоимость")
        writer = csv.DictWriter(file, delimiter=";", fieldnames=columns)
        writer.writeheader()
        writer.writerows(csv_file)
        print("Данные добавлены!")


def show_rows():
    if len(csv_file) > 0:
        print("{:<15}{:<25}{:<18}{:<12}{:<5}{:<5}{:<7}{:<5}{:<8}".format("vin_номер", "гос_номер", "марка", "модель",
                                                                         "год выпуска", "мощность двигателя", "пробег",
                                                                         "количество_владельцев", "стоимость"))
        for el in csv_file:
            print("{:<15}{:<25}{:<18}{:<12}{:<5}{:<5}{:<7}{:<5}{:<8}".format(el['vin_номер'], el['гос_номер'],
                                                                             el['марка'], el['модель'],
                                                                             el['год выпуска'],
                                                                             el['мощность двигателя'], el['пробег'],
                                                                             el['количество владельцев'],
                                                                             el['стоимость']))
