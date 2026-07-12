import pandas as pd
import matplotlib.pyplot as plt
data={
    "department":["HR","IT","HR","Finance","IT","HR","IT","FInance","HR","IT","Finance"],
    "salary":[1000,2000,4000,3000,10000,21000,18000,5000,22000,23400,1020]
}
df=pd.DataFrame(data)
print(df.groupby("department")["salary"].mean())