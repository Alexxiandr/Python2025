import csv
import matplotlib.pyplot as plt

input_f = "ChildrenOutOfSchool_Data.csv"

data = {}
years = []

with open(input_f, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        country = row["Country Name"]
        if not country or country.startswith("Data"):
            continue

        values = []

        if not years:
            for key in row.keys():
                if "[YR" in key:
                    years.append(int(key.split()[0]))


        for key in row.keys():
            if "[YR" in key:
                val = row[key]
                try:
                    values.append(float(val))
                except:
                    values.append(None)

        data[country] = values

plt.plot(years, data["Ukraine"], label="Ukraine", color="blue", linewidth=3)
plt.plot(years, data["Switzerland"], label="Switzerland", color="red", linewidth=3)

plt.title("Children out of school, primary (2009–2021)")
plt.xlabel("Year")
plt.ylabel("Number of children")
plt.legend()
plt.grid(True)
plt.show()

country = input("Введіть країну (Ukraine/Switzerland): ")

if country in data:
    plt.bar(years, data[country], color="orange")
    plt.title(f"{country} – Children out of school, primary")
    plt.xlabel("Year")
    plt.ylabel("Number of children")
    plt.grid(True, axis="y")
    plt.show()
else:
    print("Такої країни немає у файлі.")