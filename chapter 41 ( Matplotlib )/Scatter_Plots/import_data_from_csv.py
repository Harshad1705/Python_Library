import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("seaborn")

data=pd.read_csv("data.csv")
view_count=data["view_count"]
like=data["likes"]
ratio=data["ratio"]


plt.scatter(view_count , like ,  c=ratio ,  edgecolor="green" , linewidth=1.5 , alpha=0.75)

cbar=plt.colorbar()
cbar.set_label("Likes/Dislike ratio")

plt.xscale("log")
plt.yscale("log")

plt.title("Trending YouTube Chanel")
plt.xlabel("View_Count")
plt.ylabel("Total Likes")

plt.tight_layout()
plt.show()