# # # # # # class employee:
# # # # # #     language="Python"
# # # # # #     salary="120000"

# # # # # #     def __init__(self,name,salary,language):
# # # # # #      self.name=name
# # # # # #      self.salary=salary
# # # # # #      self.language=language
# # # # # #      print("Iam creating an object")

# # # # # # harry=employee("Prashant","120000","Python")    
# # # # # # print(harry.salary)
# # # # # class Employee:
# # # # #     def __init__(self):
# # # # #         print("constructor of emploee")
# # # # #         a=1

# # # # # class programmer(Employee):
# # # # #     def __init__(self):
# # # # #         print("constructor of programmer")
# # # # #         b=2
# # # # # class Manager(programmer):
# # # # #     def __init__(self):
# # # # #         super().__init__( )
# # # # #         print("constructor of manager")
# # # # #         c=3            

# # # # # o=Manager()
# # # # # dict1={'a':1,'b':2}
# # # # # dict2={'b':3,'c':4}
# # # # # dict3=dict1|dict2
# # # # # print(dict3)
# # # # with (
# # # #     open("file.txt")as f1,
# # # #     open("bad.txt")as f2
# # # # ):
# # # try:
# # #     a=int(input("enter number"))
# # #     b=int(input("enter number"))
# # #     print(a/b)

# # # except ZeroDivisionError:
# # #     print("you entered b==0")

# # # print("thank")        
# list=[3,5,7,8,9,10,11,12,13,13]
# # for index,item in enumerate(list):
# #     print(f"the item at index{index} is {item}")
# index=0
# for item in list:
#     if index==2 or index==4 or index==6:
#         print(item)
#     index+=1   
l=[1,2,3,4,5]
sq=lambda p:p*p
sqlist=map(sq,l)
print(list(sqlist))

