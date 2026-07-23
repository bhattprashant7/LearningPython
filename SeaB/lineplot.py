
# import matplotlib.pyplot as plt
# import seaborn as sns

# age=[18,19,20,21]
# salary=[18000,19000,20000,21000]
# sns.lineplot(x=age,y=salary,marker="D",linewidth=3,color="red",linestyle="--") #D=diamond and linewidth changes the thickness of the line.
# plt.title("Age vs salary")
# plt.xlabel("Age")
# plt.ylabel("Salary")
# plt.grid(True)
# plt.show()

#Using Pandas DataFrame
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# data = {
#     "age":[18,19,20,21],
#     "salary":[18000,19000,20000,21000]
# }
# df=pd.DataFrame(data)
# sns.lineplot(data=df,x="age",y="salary",color="black",linewidth=2)#data=df This tells Seaborn:"My data is stored inside the DataFrame named df.After this, Seaborn already knows all the columns in df.Column names are written as strings because Seaborn looks them up inside the DataFrame.
# plt.title("age vs salary")  
# plt.xlabel("age")
# plt.ylabel("salary")
# plt.grid(True)
# plt.show()
 

 #Hue parameter

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# data = {
#     "age":[18,19,20,21],
#     "gender":["Male","Female","Male","Female"]
# }
# df=pd.DataFrame(data)
# sns.lineplot(data=df,x="age",y="gender",color="black",linewidth=2,hue="gender") #Now Seaborn looks at the Gender column.It finds two unique values:i.e male and female.So it creates:One line for Male and One line for Female.Each line gets a different color automatically.
# plt.title("age vs gender")  
# plt.xlabel("age")
# plt.ylabel("gender")
# plt.grid(True)
# plt.show()

#style parameter
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# data = {
#     "Age": [18, 19, 20, 21, 18, 19, 20, 21],
#     "Salary": [18000, 19000, 20000, 21000,
#                17000, 18000, 19500, 20500],
#     "Gender": ["Male", "Male", "Male", "Male",
#                "Female", "Female", "Female", "Female"]
# }

# df = pd.DataFrame(data)
# sns.lineplot(data=df,x="Age",y="Salary",style="Gender") #Now Seaborn looks at the Gender  column.it finds two distinct values i.e male and female.then it draws one line style for male and another line style for female!!
# plt.show()

#Hue and style together
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# data = {
#     "Year": [2022, 2023, 2024, 2025,
#              2022, 2023, 2024, 2025],
#     "Sales": [100, 120, 150, 180,
#               90, 110, 140, 170],
#     "Company": ["A", "A", "A", "A",
#                 "B", "B", "B", "B"]
# }

# df = pd.DataFrame(data)
# sns.lineplot(data=df,x="Year",y="Sales",hue="Company",style="Company")
# plt.show()

#paratte
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_theme(style="ticks")

# data = {
#     "Age": [18, 19, 20, 21, 18, 19, 20, 21],
#     "Salary": [18000, 19000, 20000, 21000,
#                17000, 18000, 19500, 20500],
#     "Gender": ["Male", "Male", "Male", "Male",
#                "Female", "Female", "Female", "Female"]
# }
# df=pd.DataFrame(data)
# sns.lineplot(data=df,x="Age",y="Salary",hue="Gender",style="Gender",palette="bright")
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# data = {
#     "Age":[18,19,20,21],
#     "Salary":[18000,19000,20000,21000]
# }

# df = pd.DataFrame(data)

# plt.figure(figsize=(10,6))

# sns.lineplot(data=df, x="Age", y="Salary")

# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# data = {
#     "Age":[18,19,20,21],
#     "Salary":[18000,19000,20000,21000]
# }

# df = pd.DataFrame(data)
# sns.lineplot(data=df, x="Age", y="Salary",marker="o")

# plt.show()


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Age":[18,19,20,21],
    "Salary":[18000,19000,20000,21000],
    "Gender":["Male","Female","Male","Female"]
}

df = pd.DataFrame(data)
sns.lineplot(
    data=df,
    x="Age",
    y="Salary",
    hue="Gender",
    style="Gender",
    markers=True,
    dashes=False   
)
plt.show()