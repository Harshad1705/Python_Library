from matplotlib import pyplot as plt
plt.xkcd()

slices=[55,20,45,30,10]
labels=["Python","C++","JavaScript","Java","Ruby"]

color=["red","blue","yellow","green","orange"]

plt.pie(slices,labels=labels,wedgeprops={"edgecolor":"black"},colors=color)

plt.title("My pie Chart")
plt.tight_layout()
plt.show()