import csv
import matplotlib.pyplot as plt
import numpy as np

input_f = "GDP_2019_selected.csv"

countries = []
values = []

with open(input_f, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        countries.append(row["Country Name"])
        values.append(float(row["2019 GDP per capita growth (%)"]))

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

def func(pct, allvals):
    absolute = pct / 100.0 * np.sum(allvals)
    return f"{pct:.1f}%\n({absolute:.2f})"

wedges, texts, autotexts = ax.pie(
    values,
    autopct=lambda pct: func(pct, values),
    textprops=dict(color="w")
)

ax.legend(
    wedges,
    countries,
    title="Countries",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)
plt.setp(autotexts, size=8, weight="bold")

ax.set_title("GDP per capita growth (annual %) — 2019")

plt.show()