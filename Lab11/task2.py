import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv(
        "comptagevelo2010.csv",
        sep=",",
        encoding="latin1",
        parse_dates=["Date"],
        dayfirst=True
    )
except FileNotFoundError:
    print("Помилка: файл не знайдено.")

df.columns = [
    "Date", "Time", "Rachel_Papineau", "Berri1", "Maisonneuve_1",
    "Maisonneuve_2", "Brebeuf", "Parc", "CSC", "PierDup"
]
cols = ["Rachel_Papineau", "Berri1", "Maisonneuve_1", "Maisonneuve_2",
        "Brebeuf", "Parc", "CSC", "PierDup"]
df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

print(df.head())
print("Інформація про датафрейм:")
print(df.info(), "\n")
print("Описова статистика:")
print(df.describe(), "\n")

#загальна кількість за рік
df["Total"] = df[cols].sum(axis=1)
total_year = df["Total"].sum()
print(f"\nЗагальна кількість велосипедистів за 2010 рік: {int(total_year)}")

#кількість для кожної доріжки
print("\nЗагальна кількість по кожній велодоріжці:")
print(df[cols].sum(), "\n")

#найпопулярніший місяць
df["Month"] = df["Date"].dt.month
paths = ["Berri1", "Maisonneuve_1", "Brebeuf"]
print("Найпопулярніший місяць:")
for p in paths:
    best = df.groupby("Month")[p].sum().idxmax()
    print(f"{p}: найпопулярніший місяць - {best}")

#графік
plt.figure(figsize=(15, 5))
plt.plot(df["Date"], df["Berri1"], color="orange", label="Berri1")
plt.title("Використання велодоріжки Berri1 у 2010 році")
plt.xlabel("Дата")
plt.ylabel("Кількість велосипедистів")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()