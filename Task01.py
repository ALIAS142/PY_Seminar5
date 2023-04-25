# Число А в степени B.


def degree(a, b, c):
    if b != 0:
        c *= a
        b -= 1

    else:
             return c
             return degree(a, b, c)

num1 = int(input("Enter Num1  "))
num2 = int(input("Enter Num2  "))
c = 1
print(degree(num1, num2, c))
