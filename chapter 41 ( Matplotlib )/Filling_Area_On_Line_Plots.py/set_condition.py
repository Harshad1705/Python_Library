from matplotlib import pyplot as plt
import pandas as pd

data=pd.read_csv("data.csv")
ages=data["Age"]
dev_salaries=data["All_Devs"]
py_salaries=data["Python"]
djs_salaries=data["JavaScript"]

plt.plot(ages,py_salaries,label="Python")
plt.plot(ages,dev_salaries,color="#444444",linestyle="--",label="Python")

overall_median=57287
plt.fill_between(ages,py_salaries,y2=overall_median,                     # y2 describe the median change
                     where=(py_salaries>overall_median)
                     ,interpolate=True ,alpha=0.25)                 # alpha set the intensity of fill color
                                                                     
plt.legend()

plt.title("Median Salary by Ages")
plt.xlabel("Ages")
plt.ylabel("Median Salary")

plt.tight_layout()
plt.show()