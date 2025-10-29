N = 7

m = [[max(0, N - i - j) for j in range(N)] for i in range(N)]

for r in m:
    print(*r)