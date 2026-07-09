import pandas as pd
data={
    "Department":["IT","IT","HR","HR"],
    "salary":[5,10,15,20]
}
df=pd.DataFrame(data)
print(df.groupby("Department")["salary"].mean())