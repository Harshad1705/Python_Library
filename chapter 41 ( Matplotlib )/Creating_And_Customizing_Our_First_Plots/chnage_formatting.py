from matplotlib import pyplot as plt

plt.xkcd()                         

# print(plt.style.available)           for available form
# plt.style.use('fivethirtyeight')


x=[1,2,3,4,5]
first_y=[10,20,30,40,50]
second_y=[20,40,60,80,100]

plt.plot(x,first_y , color="#454545" , linestyle="-" , marker="." , linewidth=3 , label="Multiplcation of 10")     # bydefault linewidth is 1
plt.plot(x,second_y , color="b" , linestyle="-." , marker="o" , linewidth=2 , label="Multiplcation of 20")


plt.xlabel("Number")
plt.ylabel("Multiply by 10")
plt.title("MULTIPLICATION")

plt.legend()

plt.grid(True)                     # to use grid

plt.tight_layout()                 # for padding

plt.savefig("plot.png")            # to save image

plt.show()
