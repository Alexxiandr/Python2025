while True:
    n=int(input("Введіть ціле число N, де 1<N<9:"))
    if 1 < n < 9:
        break
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()