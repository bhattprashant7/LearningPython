import pandas as pd
student={
    "Name":["Ram","Hari","shyam"],
    "Age":["20","21","22"]
}
df=pd.DataFrame(student)
print(df)
df1 = pd.read_csv(r"E:\prashant\Panda\pandas\students.csv")
print(df1)
print(df[["Name","Age"]])#accessing column
 