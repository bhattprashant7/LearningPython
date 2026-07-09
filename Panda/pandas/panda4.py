import pandas as pd
data={
    "Name":["Ram","Hari","Sita"],
    "Age":[20,None,19],
    "city":["Kathmandu","Pokhara",None]
}
df=pd.DataFrame(data)
# print(df.isna())
# print(df.isna().sum())

# print(df.dropna())
df["Age"]=df["Age"].fillna(0)
print(df)