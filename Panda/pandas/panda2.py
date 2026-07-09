import pandas as pd
data={
    "Name":["Ram","shyam","Hari","sita","Gita"],
    "Age":[20,22,19,21,23],
    "Marks":["85","90","78","92","88"]
}
df=pd.DataFrame(data)
print(df)   
print(df[df['Age']>20])