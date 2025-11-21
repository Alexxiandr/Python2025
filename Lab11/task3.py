import nltk
from nltk.corpus import gutenberg, stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from collections import Counter

nltk.download("gutenberg")
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

#завантаження тексту
text = gutenberg.raw("austen-persuasion.txt")

#кількість слів
words = word_tokenize(text)
print("Загальна кількість слів у тексті:", len(words))

#10 до очищення
freq_1 = Counter(words)
top10_1 = freq_1.most_common(10)

print("\n10 найбільш вживаних слів:")
for w, c in top10_1:
    print(f"{w}: {c}")

#діаграма 1
plt.figure(figsize=(10, 5))
plt.bar([w for w, c in top10_1], [c for w, c in top10_1], color='orange')
plt.title("Топ-10 слів")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.show()

#очищення
stop_words = set(stopwords.words("english"))

clean = [
    w.lower() for w in words
    if w.isalpha() and w.lower() not in stop_words
]

#10 після очищення
freq_2 = Counter(clean)
top10_2 = freq_2.most_common(10)

print("\n10 найбільш вживаних слів після очищення:")
for w, c in top10_2:
    print(f"{w}: {c}")

#діаграма 2
plt.figure(figsize=(10, 5))
plt.bar([w for w, c in top10_2], [c for w, c in top10_2], color='green')
plt.title("Топ-10 слів (після очистки від стоп-слів і пунктуації)")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.show()