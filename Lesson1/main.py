# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

def get_number(message: str) -> int:
    while True:
        if message.isnumeric():
            return int(message)
        message = input("Введите корректное число: ")


def num_sum(number: int) -> int:
    result_sum = 0
    while number:
        result_sum += number % 10
        number //= 10
    return result_sum


print("*" * 10, "Задача 2", "*" * 10)

number = get_number(input("Введите число: "))
print(f"Сумма цифр числа {number} равна:", num_sum(number))

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

print("*" * 10, "Задача 4", "*" * 10)

number = get_number(input("Введите число, кратное 6: "))
while number % 6 != 0:
    number = get_number("Введите корректное число, кратное 6! ")
print(f"Петя и Сережа сделали по {number // 6}, Катя сделала {number // 3 * 2} журавликов")

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

print("*" * 10, "Задача 6", "*" * 10)


def check_ticket(ticket_number: int) -> bool:
    left = ticket_number // 1000
    right = ticket_number % 1000
    if num_sum(left) == num_sum(right):
        return True
    return


number = get_number(input("Введите номер билета: "))
while not 99999 < number < 1000000:
    number = get_number(input("Введите верный номер билета: "))
if check_ticket(number):
    print("Yes")
else:
    print("No")


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

print("*" * 10, "Задача 8", "*" * 10)


def check_choco(size1: int, size2: int, size_to_cut: int) -> bool:
    if size_to_cut <= size1 * size2 and any((size_to_cut % size1 == 0, size_to_cut % size2 == 0)):
        return True
    return


side1 = get_number(input("Введите количество долек шоколадки по первой стороне: "))
side2 = get_number(input("Введите количество долек шоколадки по второй стороне: "))
piece = get_number(input("Введите количество отламываемых долек: "))

if check_choco(side1, side2, piece): 
    print("Yes") 
else: 
    print("No")
