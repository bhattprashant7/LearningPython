content="""Hi everyone
we are learning I/O
using Java
I like programming in Java 
"""
def check():
     with open ("practise.txt","r") as f:
          count=1
          while(True):
               data=f.readline()
               if data == " ":
                    return -1
               if("learning" in data):
                    print(count)
                    return count
                    
               count+=1    
                          
               
check()