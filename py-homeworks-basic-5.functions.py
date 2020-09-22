documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


# Функция 1
def people():
    number_doc = str(input('Введите номер документа: '))
    for i in documents:
        if number_doc in i['number']:
            print('Имя владельца документа:', i['name'])


# Функция 2
def shelf():
    number_doc = str(input('Введите номер документа: '))
    for nym, direct in directories.items():
        if number_doc in direct:
            print(nym)
            break
    else:
        print('Такого номера документа не существует')


# Функция 3
def lists():
    for i in documents:
        x, a, b = i.values()
        print(f"{x} \"{a}\" \"{b}\"")


# Функция 4
def adds():
    type_num = str(input('Введите тип документа: ')),
    doc_num = str(input('Введите номер документа: ')),
    name_owner = str(input('Введите ФИО владельца документа: ')),
    shelf_num = str(input('Введите номер полки: ')),
    new_dict = {}
    new_dict.update({'type': type_num,
                     'number': doc_num,
                     'name': name_owner})

    documents.append(new_dict)

    for i, j in directories.items():
        if i == shelf_num:
            j.append(doc_num)
            break

    else:
        print("Такой полки не существует")

    print(documents, directories)  # Проверка


# Доп. Функция 1
def delete_doc():
    number_doc = str(input('Введите номер документа: '))
    for num in documents:
        if number_doc in num['number']:
            del num['number']

    for i, j in directories.items():
        if number_doc in j:
            j.remove(number_doc)
            break
        else:
            print('Такого номера документа не существует')
    print(documents, directories)  # Проверка


# Доп. Функция 2
def move_func():
    doc_num = str(input('Введите номер документа: '))
    shelf = str(input('Введите номер полки: '))
    shelf_num = 0
    x = directories.get(shelf)
    for i, j in directories.items():
        if doc_num in j and shelf in directories.keys():
            j.remove(doc_num)
            x.append(doc_num)

    else:
        if doc_num not in j:
            print('Указанного номера документа не существует')

        elif shelf not in directories.keys():
            print('Указанной полки не существует')

# Доп. Функция 3
def add_shelf():
    shelf = str(input('Введите номер полки: '))
    for i in directories:
        if shelf in i:
            print('Данная полка уже существует')
            break

    else:
        directories.update({shelf: []})
