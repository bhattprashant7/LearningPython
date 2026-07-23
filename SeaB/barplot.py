# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# var=sns.load_dataset("penguins")
# print(var)
# order_1=["Dream","Torgersen","Biscoe"]   #without this we will see barchat in default form i.e Torgersen,biscoe,Dream
# sns.barplot(x="island",y="bill_length_mm",data=var,hue="sex",hue_order=["Female","Male"],order=order_1) #first female will come then male
# plt.show()



# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# var=sns.load_dataset("penguins")
# sns.barplot(data=var,x="bill_length_mm",y="bill_depth_mm",orient="h") #with the help of orient you can change the orientation of bargraph i.e vertical(orient="v") or horizontal(orient="h") but for making horizontal graph both the data i.e x and y should be numerical.categorical data not allowded
# plt.show()


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set(style="darkgrid") #for grid line in seaborn usually at top
var=sns.load_dataset("penguins")
sns.barplot(data=var,x="island",y="bill_length_mm",color="black",hue="sex",palette="Accent",alpha=0.4) #saturatiom controls the intensity of color bars i.e higher saturation="brighter more vivid colors and lower saturation-lighter color" by default saturation=1 
plt.show()