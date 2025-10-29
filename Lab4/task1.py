n = int(input("n = "))

print(f"Enter {n} array elements:")
arr = [float(input()) for _ in range(n)]

max_element = max(arr)

print("Maximum element:", max_element)