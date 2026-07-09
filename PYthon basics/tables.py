# def generateTable(n):
#     table=""
#     for i in range(1, 11):
#         table += f"{n} X {i} = {n*i}\n"

#     with open(f"tables/table_{n}", "w") as f:
#         f.write(table)


# for i in range(2, 21):
#     generateTable(i)


import speech_recognition as sr
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print("listening...")
    audio=recognizer.listen(source)
    text=recognizer.recognize_google(audio)
    print("you said-",text)