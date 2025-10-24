print("lets learn user input and while loops")

i=1
while i<5:
    print("lets learn user input and while loops")
    i=i+1


age=input("whats your age: ")
age=int(age)
age=age+1
print(age)


 
#letting user end the program

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
 message = input(prompt)
 print(message)

