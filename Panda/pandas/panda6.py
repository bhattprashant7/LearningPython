import pandas as pd
data={
    "Departmnet":["IT","IT","HR","HR"],
    "salary":[5,10,15,20]
}
df=pd.DataFrame(data)
df.to_csv("employee.csv",index=False)