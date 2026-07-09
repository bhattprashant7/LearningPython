# word="Donkey"
# with open("donkey.txt","r") as f:
#     data=f.read()
#     print(data)
#     newdata=data.replace("Donkey","#####")
# with open("donkey.txt","w") as f:
#     f.write(newdata)    
with open ("log.txt","w+") as f:
    f.write("I am learning ppython\n I love learning in ptython\n coding in python is interestin")
    f.seek(0)
    content=f.read()

    words=["ppython","ptython","python"]
    for word in words:
        content=content.replace(word,"*"*len(word))
    with open ("log.txt","w") as f:
        f.write(content)    

