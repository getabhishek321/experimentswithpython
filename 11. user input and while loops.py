# print("lets learn user input and while loops")

# i=1
# while i<5:
#     print("lets learn user input and while loops")
#     i=i+1


# age=input("whats your age: ")
# age=int(age)
# age=age+1
# print(age)


 
# #letting user end the program

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#  message = input(prompt)
#  print(message)

# adding pizza ingredients

# print("enter what you would like to have")
# print("we have lehsun, pyaz, macaroni, naan")
# a=input("when you are done ordering type ok: ")
# msg=""
# b=[]

# while msg!='ok':
#    msg= input(a)
#    c=b.append(msg)
# print(b)

#cleaner version

print("Enter what you would like to have.")
print("We have lehsun, pyaz, macaroni, naan.")

b = []  # list to store all orders

while True:
    item = input("Add an item (type 'ok' when done): ").strip().lower()
    if item == 'ok':
        break
    b.append(item)

print("You ordered:", b)
