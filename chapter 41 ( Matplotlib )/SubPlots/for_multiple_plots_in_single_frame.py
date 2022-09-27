import pandas as pd
from matplotlib import pyplot as plt

data=pd.read_csv("data.csv")
ages=data["Age"]
dev_salaries=data["All_Devs"]
py_salaries=data["Python"]
js_salaries=data["JavaScript"]

fig , (ax1,ax2) = plt.subplots(nrows=2, ncols=1)

ax2.plot(ages , py_salaries , label="Python")
ax2.plot(ages , js_salaries , label="JavaScript")
ax1.plot(ages , dev_salaries , label="All Developers" , color="#444444" , linestyle="--")

ax1.legend()

ax1.set_title("Median Salary By Ages")
ax1.set_ylabel("Median Salary")

ax2.legend()

ax2.set_xlabel("Ages")
ax2.set_ylabel("Median Salary")

plt.tight_layout()
plt.show()