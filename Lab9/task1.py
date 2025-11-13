import csv

def open_csv(filename, mode):
    try:
        file = open(filename, mode, encoding="utf-8-sig")
        print(f"Файл '{filename}' успішно відкрито")
        return file
    except:
        print(f"Файл '{filename}' не знайдено або не вдалося відкрити")
        return None

input_f = "API_NY.GDP.PCAP.KD.ZG_DS2_en_csv_v2_130023.csv"
output_f = "GDP_2019_selected.csv"

file = open_csv(input_f, "r")
if file is not None:
    for _ in range(4):
        next(file)

    reader = csv.DictReader(file)
    print("\nGDP per capita growth (annual %) — 2019:\n")

    for row in reader:
        country = row["Country Name"]
        value = row["2019"]
        if country:
            print(f"{country}: {value}")

    file.close()

file = open_csv(input_f, "r")
if file is not None:
    for _ in range(4):
        next(file)

    reader = csv.DictReader(file)
    countries = input("\nВведіть назви країн через кому: ").split(",")
    countries = [c.strip() for c in countries]

    found = False
    with open(output_f, "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(["Country Name", "2019 GDP per capita growth (%)"])

        for row in reader:
            name = row["Country Name"]
            if name in countries:
                value = row["2019"]
                print(f"{name}: {value}")
                writer.writerow([name, value])
                found = True

    file.close()
    if not found:
        print("Жодна з вказаних країн не знайдена у файлі.")
    else:
        print(f"\nРезультати записано у файл '{output_f}'.")