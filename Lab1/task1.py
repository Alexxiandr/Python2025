a=float(input("Введіть додатнє a: "))
while a<=0:
    a=float(input("Число a повинно бути додатнім, a: "))
b=float(input("Введіть додатнє b: "))
while b<=0:
    b = float(input("Число b повинно бути додатнім, b: "))
if a>b:
    x = a*b-3
elif a==b:
    x = 2
else:
    x=(a**3 +1)/b
print("X =",x)