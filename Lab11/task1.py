import pandas as pd

employees = [
    {"Surname": "Іванов", "Address": "вул. Центральна, 15", "Position": "Менеджер", "Salary": 18000, "Experience": 3},
    {"Surname": "Павленко", "Address": "вул. Соборна, 42", "Position": "Менеджер", "Salary": 19500, "Experience": 5},
    {"Surname": "Рибак", "Address": "просп. Перемоги, 8", "Position": "Менеджер", "Salary": 21000, "Experience": 4},
    {"Surname": "Петров", "Address": "вул. Київська, 22", "Position": "Програміст", "Salary": 35000, "Experience": 5},
    {"Surname": "Кравченко", "Address": "вул. Миру, 18", "Position": "Програміст", "Salary": 39000, "Experience": 7},
    {"Surname": "Кубиків", "Address": "вул. Хрещатик, 2", "Position": "Програміст", "Salary": 37000, "Experience": 3},
    {"Surname": "Сидоров", "Address": "вул. Шевченка, 44", "Position": "Дизайнер", "Salary": 22000, "Experience": 2},
    {"Surname": "Мельник", "Address": "вул. Коцюбинського, 14", "Position": "Дизайнер", "Salary": 24000, "Experience": 4},
    {"Surname": "Кузін", "Address": "вул. Грушевського, 11", "Position": "HR", "Salary": 16000, "Experience": 2},
    {"Surname": "Куравльов", "Address": "вул. Козацька, 9", "Position": "HR", "Salary": 15500, "Experience": 3},
    {"Surname": "Кудін", "Address": "вул. Миру, 5", "Position": "Аналітик", "Salary": 28000, "Experience": 6},
    {"Surname": "Кульков", "Address": "вул. Соборна, 18", "Position": "Бухгалтер", "Salary": 20000, "Experience": 7},
    {"Surname": "Семенов", "Address": "вул. Франка, 30", "Position": "Бухгалтер", "Salary": 19000, "Experience": 4}
]

df = pd.DataFrame(employees)
print(df)

print("\nПерші 3 рядки:")
print(df.head(3))

print("\nТипи даних:")
print(df.dtypes)

print("\nРозмір (рядки, стовпці):")
print(df.shape)

print("\nОписова статистика:")
print(df.describe())

#стовпець премія 10%
df["Bonus"] = df["Salary"] * 0.10
print("\nПісля додавання стовпця з премією:")
print(df)

#фільтрація
salary_filter = df[df["Salary"] > 20000]
print("\nСпівробітники з зарплатою > 20 000:")
print(salary_filter)

#сортування
salary_sort = df.sort_values(by="Salary", ascending=False)
print("\nСортування за зарплатою (спадання):")
print(salary_sort)

#групування
salary_group = df.groupby("Position")["Salary"].mean()
print("\nСередня зарплата по посадах:")
print(salary_group)

print("\nМаксимальна зарплата у компанії:")
print(df["Salary"].max())

print("\nКількість унікальних посад:")
print(df["Position"].nunique())