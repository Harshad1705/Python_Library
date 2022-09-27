from matplotlib import pyplot as plt
plt.xkcd()

x=[1,2,3,4,5]
first_y=[10,20,30,40,50]


plt.bar(x,first_y,color="#666666")


plt.xlabel("Number")
plt.ylabel("Multiply by 10")
plt.title("MULTIPLICATION")

plt.legend(["Multiplcation of 10","Multiplication of 20"])

plt.show()