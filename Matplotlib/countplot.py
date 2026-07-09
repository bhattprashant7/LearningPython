import matplotlib.pyplot as plt
import pandas as pd
Data={
    "Department":["HR","IT","Finance","IT","HR","Finance","IT"]
}
df=pd.DataFrame(Data)
count=df["Department"].value_counts()
print(count)
plt.bar(count.index,count,color=["red",'green','black'])
plt.show()