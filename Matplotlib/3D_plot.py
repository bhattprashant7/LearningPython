# import pandas as pd
# import matplotlib.pyplot as plt

# data = {
#     "Age":[18,19,20,21,22],
#     "Salary":[1000,2000,5000,7000,9000],
#     "Experience":[1,2,4,5,8]
# }

# df = pd.DataFrame(data)

# fig = plt.figure() #creates a figure

# ax = fig.add_subplot(111, projection="3d") #111=1 row,1 column,1st graph(place where graph is to be plotted)

# ax.scatter(
#     df["Age"],
#     df["Salary"],
#     df["Experience"]
# )

# ax.set_xlabel("Age")
# ax.set_ylabel("Salary")
# ax.set_zlabel("Experience")

# plt.title("3D Scatter Plot")

# plt.show()

#3D line plot
# import pandas as pd
# import matplotlib.pyplot as plt
# fig=plt.figure()
# ax=fig.add_subplot(111,projection="3d")
# x = [1,2,3,4,5]
# y = [2,3,5,7,9]
# z = [1,4,2,6,8]
# ax.plot(x,y,z)
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_zlabel("z")
# plt.title("Lineplot")
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={"projection":"3d"})

x = np.linspace(-5,5,50) #create 50 equally spaced number between -5 and 5

y = np.linspace(-5,5,50)

X, Y = np.meshgrid(x,y)

Z = X**2 + Y**2

ax.plot_surface(X,Y,Z)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()