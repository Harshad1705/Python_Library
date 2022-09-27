import pandas as pd
from matplotlib import pyplot as plt

data=pd.read_csv("data.csv")
ages=data["Age"]
dev_salaries=data["All_Devs"]
py_salaries=data["Python"]
js_salaries=data["JavaScript"]

fig , ax = plt.subplots()

ax.plot(ages , py_salaries , label="Python")
ax.plot(ages , js_salaries , label="JavaScript")
ax.plot(ages , dev_salaries , label="All Developers" , color="#444444" , linestyle="--")

ax.legend()

ax.set_title("Median Salary By Ages")
ax.set_xlabel("Ages")
ax.set_ylabel("Median Salary")

plt.tight_layout()
plt.show()