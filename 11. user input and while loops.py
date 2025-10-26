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

# print("welcome to age based movie theater")
# print("type done to quit: ")


# while True:
#     a=input("enter your age: ")

#     if a=='done':
#         break;
#     a=int(a)
#     if a<=3:
#         print("your ticket is free, type done to quit")
#     elif a>3 and a<=18:
#         print("it will cost you full cost of 500, type done to quit")
#     elif a>=18 and a<=50:
#         print("it will cost you 200, type done to quit")
#     elif a=="done": 
#         break;

# #cleaner version

# print("Welcome to the age-based movie theater!")
# print("Type 'done' to quit.\n")

# while True:
#     a = input("Enter your age: ").strip().lower()

#     if a == 'done':
#         print("Thank you for visiting!")
#         break

#     if not a.isdigit():
#         print("Please enter a valid number or 'done' to quit.")
#         continue

#     age = int(a)

#     if age <= 3:
#         print("Your ticket is free.")
#     elif 3 < age <= 18:
#         print("Your ticket will cost ₹500.")
#     elif 18 < age <= 50:
#         print("Your ticket will cost ₹200.")
#     else:
#         print("Your ticket will cost ₹300.")  # For seniors, optional

# three exits

# Use a conditional test in the while statement to stop the loop. 
# • Use an active variable to control how long the loop runs. 
# • Use a break statement to exit the loop when the user enters a 'quit' value

# i=1

# while i<=5:
#     print("going good")
#     i=i+1
#     if i==5:
#         a=input(f"do you want to continue: press 'y' or 'n' ")
#         if a=='y':
#             continue
#         elif a=='n':
#             break;

# more effective

# print("Loop exercise demo")

# active = True     # active variable to control the loop
# i = 1             # counter, optional

# while active:     # conditional test
#     print(f"Round {i}: going good")

#     a = input("Type 'y' to keep going, 'n' to stop, or 'quit' to exit immediately: ").strip().lower()

#     if a == 'quit':
#         print("Quitting loop via break…")
#         break                        # requirement 3
#     elif a == 'n':
#         active = False               # turns off the loop
#     elif a == 'y':
#         i += 1                       # continue to next round
#         continue
#     else:
#         print("Invalid input, please type y / n / quit.")

# print("Loop finished.")

# using while loop with two lists

# unconfirmed_users=['a','b','c','d']
# confirmed_users=[]

# while unconfirmed_users!=[]: # while unconfirmed_users: this would also mean the list is not empty
#     print(f"checking current user: {unconfirmed_users[-1]}")
#     check=unconfirmed_users.pop()
#     confirmed_users.append(check)
# print(f"so these are confirmed users: {confirmed_users}")


# removing specific items from a list

people=['dog', 'cat', 'dogesh', 'catesh', 'horsy', 'cati kumar']

# while 'cat' in people:
#     people.pop()

#     print(people)

    #so this didnt work as expected, its removing all items till it encounters cat

# while 'cat' in people:
#     people.remove('cat')

# print(people) # this worked as expected

# how about we remove all occurences of cat in list, something sort of a wild card search

# a= people.find('*cat*')
# while a in people:
#     b=people.remove({a})
#     print (people) #this DOESN't WORK AT ALL find doesnt exist with lists.

#achieving the desired output way 1

people = ['dog', 'cat', 'dogesh', 'catesh', 'horsy', 'cati kumar']

people = [p for p in people if 'cat' not in p]

print(people)


#achieving the desired output way 2, loop approach

people = ['dog', 'cat', 'dogesh', 'catesh', 'horsy', 'cati kumar']

i = 0
while i < len(people):
    if 'cat' in people[i]:
        people.pop(i)       # remove the element at this index
    else:
        i += 1              # only move forward when not removing

print(people)

#achieving the desired output way 3, Using filter() (functional approach)

people = ['dog', 'cat', 'dogesh', 'catesh', 'horsy', 'cati kumar']

people = list(filter(lambda x: 'cat' not in x, people))
print(people)
