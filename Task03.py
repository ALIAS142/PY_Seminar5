# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)
# Input: 5 Output: yes

n = int(input("Enter number:  "))


def simple_number(n):
    # i = 2
    for i in range(2, n):
        if n % i == 0:
            return 'no'
    return 'yes'


print(simple_number(n))
