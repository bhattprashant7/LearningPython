import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
var=sns.load_dataset("tips")
#print(var)
# sns.countplot(x="sex",data=var,hue="smoker") #count plot
# sns.countplot(y="sex",data=var,hue="smoker") #for horizontal graphs
sns.barplot(x="sex",y="size",data=var,saturation=0.5)
plt.show()