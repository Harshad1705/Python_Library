import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

ages = [18,19,21,25,26,26,30,32,38,45,55]
bin=[10,20,30,40,50,60]

plt.hist(ages,bins=bin,edgecolor="black")

plt.title("Age of Respondent")
plt.xlabel("Ages")
plt.ylabel("Total Respodent")

plt.tight_layout()
plt.show()