import seaborn as sns
import matplotlib.pyplot as plt
var=sns.load_dataset("penguins").head(20)
#print(var)
sns.scatterplot(data=var,x="bill_length_mm",y="bill_depth_mm",hue="sex",style="sex",size="sex",sizes=(10,50),palette="Set1",alpha=0.4) #sizes specifies the minimum and maximum marker size that Seaborn should use. and size=sex will specify size will differ w.r.t sex
plt.show()