import csv
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter

plt.xkcd()

with open("data.csv") as csv_file:
    csv_reader=csv.DictReader(csv_file)
    
    language_counter=Counter()
    
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(";"))

# print(language_counter)

language=[]
popularity=[]

for item in language_counter.most_common(15):
    language.append(item[0])
    popularity.append(item[1])

plt.barh(language,popularity)

plt.title("Most Poular Languages")
plt.xlabel("Number of people used")

plt.tight_layout()
plt.show()