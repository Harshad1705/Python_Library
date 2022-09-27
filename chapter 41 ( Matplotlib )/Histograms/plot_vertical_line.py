import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data=pd.read_csv("data.csv")
ages=data["Age"]
ids=data["Responder_id"]

bin=[10,20,30,40,50,60,70,80,90,100]

plt.hist(ages,bins=bin,edgecolor="black")


median_age=29
color="#fc4f30"

plt.axvline(median_age,color=color,linewidth=2)

plt.title("Age of Respondent")
plt.xlabel("Ages")
plt.ylabel("Total Respodent")

plt.tight_layout()
plt.show()