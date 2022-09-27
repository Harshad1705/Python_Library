import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("seaborn")

x=[1,2,3,4,5]
y=[3,6,9,12,15]

plt.scatter(x,y)

plt.tight_layout()
plt.show()