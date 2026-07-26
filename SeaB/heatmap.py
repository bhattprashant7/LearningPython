# import seaborn as sns
# import matplotlib.pyplot as plt

# data = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# sns.heatmap(data,annot=True,cmap="Blues")
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# var=np.linspace(1,10,20).reshape(4,5) #reshape will arrange data into 4 rows and 5 columns
# #print(var)
# sns.heatmap(var)
# plt.show()


# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# var=sns.load_dataset("anagrams").drop("attnr",axis=1).head(10)
# print(var)
# sns.heatmap(var,annot=True,cmap="Blues") # annot=True i.e now every cell will display its corresponding value!
# plt.show()


# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# var=np.linspace(1,10,10).reshape(2,5)
# arr=np.array([
#     ["a0","a1","a2","a3","a4"],
#     ["b0","b1","b2","b3","b4",]
# ])
# sns.heatmap(var,cmap="Blues",annot=arr,fmt="s") #if arr was not used we will get the output as above but with arr introduction and if we want to fill the cells of heatmap with the different values i.e wanna change it we do as above i.e annot="arr",format(fmt)="s"(string)

# plt.show()


# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# var=np.linspace(1,10,10).reshape(2,5)
# y={
#     "fontsize":50,
#     "color":"r"
# }
# sns.heatmap(var,annot=True,annot_kws=y,linewidths=10,linecolor="y",cbar=False,xticklabels=False,yticklabels=False) #with annot=true and annot_kws=y the number in the cell of the heatmap will change its properties i.e fontsize to 50 and color to red and linewidth =10 increases the distance between cells and cbar means color bar which is present at right side of the heatmap...xticklabel and yticklabel False will remove the labels at x and y axis

# plt.show()

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
var=np.linspace(1,10,10).reshape(2,5)
v=sns.heatmap(var,annot=True,xticklabels=False,yticklabels=True)
v.set(xlabel="Python",ylabel="heatmap") #set the x and y axis label!we can also set it using plt.xlabel="Python" and plt.ylabel="heatmap" but using seaborn we can do this too
sns.set(font_scale=1)
plt.show()