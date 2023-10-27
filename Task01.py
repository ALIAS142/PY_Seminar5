# Даны два целых числа A И B. Вывести ысе числа от A До B включительно по возрастанию, если A < B и наоборот.

def numbers(a, b):
    if a == b:
        return b
    if a < b:
        return f'{a} {numbers(a + 1, b)}'
    if a > b:
        return f'{numbers(a - 1, b)} {b}'


print(numbers(10, 1))
