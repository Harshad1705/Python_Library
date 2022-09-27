import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter

plt.xkcd()

data=pd.read_csv("data.csv")
ids=data['Responder_id']
language_response=data["LanguagesWorkedWith"]

language_counter=Counter()

for row in language_counter:
    language_counter.update(row.split(";"))


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