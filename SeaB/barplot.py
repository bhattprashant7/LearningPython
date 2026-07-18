import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
var=sns.load_dataset("penguins")
print(var)
order_1=["Dream","Torgerson","Biscoe"]
sns.barplot(x="island",y="bill_length_mm",data=var,hue="sex",order=order_1)
plt.show()

