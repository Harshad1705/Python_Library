import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("seaborn")

x=[1,2,3,4,5]
y=[3,6,9,12,15]

color=[5,10,15,20,25]
size=[100,200,300,400,500]

plt.scatter(x,y , s=size , c=color , cmap="Greens" , marker=">" , edgecolor="k" , linewidth=1.5 , alpha=0.75)
                            # cmap ---> color map

cbar=plt.colorbar()
cbar.set_label("Shades")

plt.tight_layout()
plt.show()