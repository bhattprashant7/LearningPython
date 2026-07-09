# import matplotlib.pyplot as plt
# import pandas as pd
# data = {
#     "salary": [
#         25000,26000,28000,29000,31000,32000,35000,
#         40000,45000,48000,50000,55000,70000,
#         80000,85000,90000,91000,92000,100000,
#         91000,89000,50000,28000,250000
#     ]
# }
# df=pd.DataFrame(data)
# plt.boxplot(df["salary"])
# plt.title("Salary Distribution")
# plt.ylabel("Salary")
# plt.grid(axis='y')
# plt.show()
import matplotlib.pyplot as plt
import pandas as pd
data = {
    "values": [
        22,25,17,19,33,60,23,17,20,28 #60 is outlier
    ]
}
df=pd.DataFrame(data)
df.loc[0]=5 #22 is replaced with 5
df.drop(index=0,inplace=True) #row 0 is permanently removed and no new dataFrame created
plt.boxplot(df["values"])
plt.title("Values")
plt.ylabel("y_axis")
plt.grid(axis='y')
plt.show()