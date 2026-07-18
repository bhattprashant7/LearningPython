import seaborn as sns
import matplotlib.pyplot as plt
dat=sns.load_dataset("penguins").head(20)#for working with 20 data only
print(dat)
sns.lineplot(x="bill_length_mm",y="bill_depth_mm",data=dat,hue="sex",style="sex",palette="Accent",markers=["o",">"])
plt.show()