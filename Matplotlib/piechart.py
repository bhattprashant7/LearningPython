# import matplotlib.pyplot as plt
# department=["IT","HR","Sales","Finance"]
# employee=[40,20,30,10]
# plt.pie(employee,labels=department,  autopct="%1.1f%%")
# plt.show()

import matplotlib.pyplot as plt
import pandas as pd
data={
    "department":["IT","HR","IT","Sales","HR","IT","Finance","Sales"]
}
df=pd.DataFrame(data)
counts=df["department"].value_counts() #select the department column and count each department
print(counts)  
plt.pie(counts,labels=counts.index,autopct="%1.1f%%",explode=[0,0.1,0,0]) #explode i.e second one i.e HR gets departed from first one with a a distance of 0.1
plt.axis("equal") #makes the pie chart a proper circle 
plt.show()