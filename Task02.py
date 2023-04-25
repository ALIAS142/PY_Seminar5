# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность
# в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input:    2 -> 3 4 Output: 4 3

N = int(input("Enter number:    "))
x = 1
while x <= N:
    print(x)
    x+=1
#
# N = int(input("Enter number:    "))
#
#
def rev_seq(N):
    if N == 1:
        return N
    else:
        return N, rev_seq(N - 1)


print(rev_seq(N))




#
# def rotate (n):
# if n == 0:
# return " "
# else:
# a = int(input("Value "))
# return rotate(n-1) + f" {a} "
#
#
# n = int(input("Enter n: "))
#
# print(rotate(n))

