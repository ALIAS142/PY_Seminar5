# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу,
# которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1
#
# n = int(input("Enter number:  "))
#
# from random import randint
#
# list = [randint(1, 5) for i in range(n)]
# print(list)
#
# max_number = max(list)
# print(max_number)
#
# min_number = min(list)
# print(min_number)
#
#
# def change_max_min(list):
#     # temp = 0
#     # temp == min_number
#     min_number == max_number
#     max_number == min_number
#
#
# print(change_max_min(list))


seq = [2, 3, 2, 4, 5]
mx = 0
mn = 6
for el in seq:
    if el > mx:
        mx = el
    if el < mn:
        mn = el
for i in range(len(seq)):
    if seq[i] == mn:
        seq[i] = mx

print(*seq)
