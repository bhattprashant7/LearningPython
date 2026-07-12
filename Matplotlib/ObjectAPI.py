# import matplotlib.pyplot as plt

# x = [1,2,3,4]
# y = [10,20,15,30]

# fig, ax = plt.subplots()

# ax.plot(x, y)

# ax.set_title("Sales")
# ax.set_xlabel("Month")
# ax.set_ylabel("Sales")

# plt.show()
import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2) #1 row,2 column #ax[0] means first subplot and ax[1] means second subplot
ax[0].plot([1,2,3],[2,4,6])
ax[0].set_title("First")
plt.savefig("line.png") #saves the pic in the format png
ax[1].scatter([1,2,3],[2,4,6])
ax[1].set_title("second")
plt.show()