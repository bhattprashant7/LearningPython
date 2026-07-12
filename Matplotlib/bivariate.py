
#sort age
# import pandas as pd
# data={
#     "age":[18,14,19,12,9]
# }
# df=pd.DataFrame(data)
# print(df.sort_values("age"))
   

#numerical vs Categorical data
import pandas as pd
import matplotlib.pyplot as plt
data={
    "department":["HR","IT","HR","Finance","IT","HR","IT","FInance","HR","IT","Finance"],
    "salary":[1000,2000,4000,3000,10000,21000,18000,5000,22000,23400,1020]
}
df=pd.DataFrame(data)
# print(df)
df2=df[df["department"]=="HR"] #for getting only HR department and its salary
df3=df[df["department"]=="IT"]
df4=df[df["department"]=="Finance"]
plt.boxplot([df2["salary"],df3["salary"],df4["salary"]],label=["HR","IT","Finance"])
plt.legend()
plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
# data={
#     "department":["HR","IT","HR","Finance","IT","HR","IT","Finance","HR","IT","Finance"],
#     "salary":[1000,2000,4000,3000,10000,21000,18000,5000,22000,23400,1020]
# }
# df=pd.DataFrame(data)
# sal_bydept=df.groupby("department")["salary"].mean()
# print(sal_bydept)
# plt.pie(sal_bydept,labels=sal_bydept.index,autopct="%1.2f",shadow=True)
# plt.show()

