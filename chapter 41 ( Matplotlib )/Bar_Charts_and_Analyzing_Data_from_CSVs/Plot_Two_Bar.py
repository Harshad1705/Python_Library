import numpy as np
from matplotlib import pyplot as plt


x=[1,2,3,4,5]
x_index=np.arange(len(x))
width=0.25

first_y=[10,20,30,40,50]
second_y=[20,40,60,80,100]

plt.bar(x_index-width,first_y,width=width)
plt.bar(x_index,second_y,width=width)



plt.xticks(ticks=x_index,label=x)

plt.xlabel("Number")
plt.ylabel("Multiply by 10")
plt.title("MULTIPLICATION")

plt.legend(["Multiplcation of 10","Multiplication of 20"])

plt.show()