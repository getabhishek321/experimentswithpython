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

# print("Enter what you would like to have.")
# print("We have lehsun, pyaz, macaroni, naan.")

# b = []  # list to store all orders

# while True:
#     item = input("Add an item (type 'ok' when done): ").strip().lower()
#     if item == 'ok':
#         break
#     b.append(item)

# print("You ordered:", b)


# # movie tickets

print("welcome to age based movie theater")
print("type done to quit: ")


while True:
    a=input("enter your age: ")

    if a=='done':
        break;
    a=int(a)
    if a<=3:
        print("your ticket is free, type done to quit")
    elif a>3 and a<=18:
        print("it will cost you full cost of 500, type done to quit")
    elif a>=18 and a<=50:
        print("it will cost you 200, type done to quit")
    elif a=="done": 
        break;

#cleaner version

print("Welcome to the age-based movie theater!")
print("Type 'done' to quit.\n")

while True:
    a = input("Enter your age: ").strip().lower()

    if a == 'done':
        print("Thank you for visiting!")
        break

    if not a.isdigit():
        print("Please enter a valid number or 'done' to quit.")
        continue

    age = int(a)

    if age <= 3:
        print("Your ticket is free.")
    elif 3 < age <= 18:
        print("Your ticket will cost ₹500.")
    elif 18 < age <= 50:
        print("Your ticket will cost ₹200.")
    else:
        print("Your ticket will cost ₹300.")  # For seniors, optional
