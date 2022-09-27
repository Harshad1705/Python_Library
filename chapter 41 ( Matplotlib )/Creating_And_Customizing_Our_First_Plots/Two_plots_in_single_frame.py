from matplotlib import pyplot as plt

x=[1,2,3,4,5]
first_y=[10,20,30,40,50]
second_y=[20,40,60,80,100]

plt.plot(x,first_y)
plt.plot(x,second_y)


plt.xlabel("Number")
plt.ylabel("Multiply by 10")
plt.title("MULTIPLICATION")

plt.legend(["Multiplcation of 10","Multiplication of 20"])

plt.show()