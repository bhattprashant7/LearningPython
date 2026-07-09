import pandas as pd
data={
    "Departmnet":["IT","IT","HR","HR"],
    "salary":[5,10,15,20]
}
df=pd.DataFrame(data)
df["Grade"]=["A","B","C","D"]
print(df )
print(df.iloc[0])#accessing rows
print(df[df["salary"]>10])
