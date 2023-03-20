def get_operation() -> int:
    operation = input("Введите операцию:\n\t1: добавить запись\n\t2: найти запись\n\t3: изменить запись\n\t4: удалить запись\n\t5: выход\nВыберите пункт меню: ")
    while operation not in ("1", "2", "3", "4", "5"):
        operation = input("Введите корректный пункт меню (цифра от 1 до 5): ")
    return int(operation)


def create(new_contact):
    with open("file.txt", "a", encoding="utf-8") as file:
        file.write(new_contact + "\n")


def check_contact(string):
    with open("file.txt", "r+", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if string in line:
                return True
        return False


def get_list(query):
    with open("file.txt", "r", encoding="utf-8") as file:
        print(query)
        list_lines = []
        for line in file:
            if query in line:
                list_lines.append(line)
        return list_lines
    

def del_record(record):
    with open("file.txt", "r", encoding="utf-8") as file:
        old_data = file.read()
    new_data = old_data.replace(record, "")
    with open("file.txt", "w", encoding="utf-8") as file:
        file.write(new_data)


def change_record(old_record):
    del_record(old_record)
    struct = ["Фамилия: ", "Имя: ", "Отчество: ", "Телефон: "]
    string = " ".join([input(struct[i]) for i in range(4)])
    create(string)

    

        


