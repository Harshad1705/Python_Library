import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data=pd.read_csv("data.csv")
ages=data["Age"]
ids=data["Responder_id"]

plt.hist(ages,bins=10,edgecolor="black")

plt.title("Age of Respondent")
plt.xlabel("Ages")
plt.ylabel("Total Respodent")

plt.tight_layout()
plt.show()