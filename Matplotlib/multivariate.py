#Multivariate analysis
#bubble plot
import pandas as pd
import matplotlib.pyplot as plt
data={
    "department":["HR","IT","HR","Finance","IT","HR","IT","FInance","HR","IT","Finance"],
    "age":[18,19,17,25,23,16,20,29,25,24,19],
    "salary":[1000,2000,4000,3000,10000,21000,18000,5000,22000,23400,1020],
    "experience":[1,2,3,2,5,4,8,12,6,4,9]
}
df=pd.DataFrame(data)
# plt.scatter(df["age"],df["salary"],s=df["experience"]*20,color="red")
# plt.xlabel("Age")
# plt.ylabel("salary")
# plt.title("Experience of diff departments")
# plt.show()
hr = df[df["department"] == "HR"]

it = df[df["department"] == "IT"]
finance = df[df["department"] == "Finance"]
plt.scatter(hr["age"], hr["salary"],
            s=hr["experience"]*20,
            color="red",
            label="HR")

plt.scatter(it["age"], it["salary"],
            s=it["experience"]*20,
            color="blue",
            label="IT")

plt.scatter(finance["age"], finance["salary"],
            s=finance["experience"]*20,
            color="green",
            label="Finance")

plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Bubble Plot by Department")
plt.legend()

plt.show()