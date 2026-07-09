import matplotlib.pyplot as plt
import pandas as pd
data={
    "salary":[25000,26000,28000,29000,31000,32000,35000,40000,45000,48000,
              50000,55000,70000,80000,85000,90000,91000,92000,100000,91000,89000,50000,28000]

}
df=pd.DataFrame(data)
plt.hist(data["salary"],bins=20,color="red")
plt.title("Salaries of employee")
plt.xlabel("salary")
plt.ylabel("No.of employee")
plt.show()


