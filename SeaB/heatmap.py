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


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

var=sns.load_dataset("anagrams").drop("attnr",axis=1).head(10)
print(var)
sns.heatmap(var,annot=True,cmap="Blues") # annot=True i.e now every cell will display its corresponding value!
plt.show()