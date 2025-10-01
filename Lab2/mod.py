def expression_y(n):
    y = 1
    for i in range(1, 2 * n, 2):
        y *= i
    return y