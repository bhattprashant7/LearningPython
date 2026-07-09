# import matplotlib.pyplot as plt
# import pandas as pd
# # print(matplotlib.__version__)
# x=[1,2,3]
# y=[4,5,6]
# plt.plot(x,y)
# # plt.grid()
# # plt.show()
# data={
#     "salary":[25000,26000,28000,29000,31000,32000,35000,40000,45000,48000,
#               50000,55000,70000,80000,85000,90000,91000,92000,100000,91000,89000,50000,28000]

# }
# df=pd.DataFrame(data)
# print(df.head())
# print(df.shape)
# plt.plot(df["salary"],color='red',marker='o',linestyle="--",linewidth="2")
# plt.grid()
# plt.show()


import matplotlib.pyplot as plt
import pandas as pd

data = {
    "salary":[25000,26000,28000,29000,31000,32000,35000,40000,45000,48000],
    "age":[19,20,17,14,28,23,28,23,16,11]
}

df = pd.DataFrame(data)

# Sort by age
sort_age = df.sort_values("age")
print(sort_age) #sort_values() returns the entire DataFrame, not just the column you sorted by.

# Plot age vs salary
# plt.plot(sort_age["age"], sort_age["salary"],
#          color="red", marker="o")

# plt.xlabel("Age")
# plt.ylabel("Salary")
# plt.title("Age vs Salary")
# plt.grid(True)

# plt.show()

plt.bar(sort_age["age"],sort_age["salary"]) #barchart (bins not used ,bins used for histogram only not barchart)
plt.show()


