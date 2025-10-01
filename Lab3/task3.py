s = input("Введіть речення: ")

print("Слова без 'привіт':")
for w in s.split():
    if w.lower() != "привіт":
        print(w)