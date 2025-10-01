import math

def expression_z(alpha):
    z = math.cos(alpha) + math.cos(2 * alpha) + math.cos(6 * alpha) + math.cos(7 * alpha)
    return z

def expression_y(n):
    y = 1
    for i in range(1, 2 * n, 2):
        y *= i
    return y

alpha = float(input("Введіть значення α: "))
print("Результат z =", expression_z(alpha))

n = int(input("Введіть натуральне число n: "))
print("Результат y =", expression_y(n))