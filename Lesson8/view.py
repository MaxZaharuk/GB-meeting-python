import operations


def add_contact():
    struct = ["Фамилия: ", "Имя: ", "Отчество: ", "Телефон: "]
    string = " ".join([input(struct[i]) for i in range(4)])
    if not operations.check_contact(string=string):
        operations.create(string)
        print("***Запись успешно добавлена***\n")
    else:
        print("***Такой контакт уже есть!***\n")
        print("-" * 20)


def get_contact():
    query = input("Введите что вы ищете: ")
    if not operations.check_contact(query):
        print("***В записной книжке таких данных нет!***\n")
    else:
        data = operations.get_list(query)
        print("Записи по вашему запросу:")
        for i in data:
            print(i)
        print("-" * 20)


def set_contact():
    query = input("Введите какой контакт вы хотите поменять: ")
    if not operations.check_contact(query):
        print("***В записной книжке таких данных нет!***\n")
    else:
        data = operations.get_list(query)
        print("Записи по вашему запросу:")
        n = 1
        for i in data:
            print(n, "\t\t", i)
            n += 1
        choice = input("Выберите номер записи, которую хотите изменить: ")
        while choice not in [str(i) for i in range(1, len(data) + 1)] and choice != "0":
            choice = input("Введите корректный номер записи или 0 для возврата в меню: ")
        if int(choice) == 0:
            return
        operations.change_record(data[int(choice) - 1])
        print("***Запись успешно изменена!***\n")


def del_contact():
    query = input("Введите какой контакт вы хотите удалить: ")
    if not operations.check_contact(query):
        print("***В записной книжке таких данных нет!***\n")
    else:
        data = operations.get_list(query)
        print("Записи по вашему запросу:")
        n = 1
        for i in data:
            print(n, i)
            n += 1
        choice = input("Выберите номер записи, которую хотите удалить: ")
        operations.del_record(data[int(choice) - 1])
        print("***Запись успешно удалена!***\n")