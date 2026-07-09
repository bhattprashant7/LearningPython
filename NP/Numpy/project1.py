import pandas as pd
df = pd.read_csv(r"E:\prashant\NP\Numpy\__pycache__\students.csv")
print(df)
# print(df.head())#head()shows first five rows
# print(df.tail())#tail()shows last five rows
# print(df.info())
print(df["Name"])#shows only Name column
print(df[["Name","Marks"]])#notice the double bracket {for accessing multiple rows we use double brackets}
print(df[df["Marks"]>80])
print(df[df["City"]=="Kathmandu"])
print(df[(df["City"]=="Pokhara") & (df["Marks"]>85)]) #show students from Pokhara who scored more than 85
print(df["Marks"].mean())
print(df["Marks"].max())#who scored the highest marks
print(df.groupby("City")["Marks"].mean()) #average marks in each city
print(df.groupby("City")["Name"].count()) #How many students are there in each city

