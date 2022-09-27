import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

ages = [18,19,21,25,26,26,30,32,38,45,55]

plt.hist(ages,bins=5,edgecolor="black")

plt.title("Age of Respondent")
plt.xlabel("Ages")
plt.ylabel("Total Respodent")

plt.tight_layout()
plt.show()