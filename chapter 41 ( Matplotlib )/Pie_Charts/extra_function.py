from matplotlib import pyplot as plt
plt.xkcd()

slices=[55,20,45,30,10]
labels=["Python","C++","JavaScript","Java","Ruby"]

color=["red","blue","yellow","green","orange"]

explode=[0.1,0,0,0,0]                # that percentage of radius exploded out from pie  

plt.pie(slices , labels=labels , explode=explode , wedgeprops={"edgecolor":"black"} , colors=color , shadow=True , autopct="%1.1f%%" )

plt.title("My pie Chart")
plt.tight_layout()
plt.show()