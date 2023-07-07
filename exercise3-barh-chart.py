import csv
from collections import Counter

from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

with open("data.csv") as data_file:
    data_reader = csv.DictReader(data_file)

    language_counter = Counter()
    for obj in data_reader:
        language_counter.update(obj['LanguagesWorkedWith'].split(";"))

    languages, popularity = zip(*language_counter.most_common(15))

languages, popularity = list(languages), list(popularity)
languages.reverse()
popularity.reverse()
plt.barh(languages, popularity)
plt.xlabel("Num of people who use")
plt.ylabel("Programming Languages")
plt.title("Programming Languages popularity")
plt.legend()
plt.tight_layout()
plt.show()
