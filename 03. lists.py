                         

# bicycles=['Trek','Cannondale','Redline','Specialized']
# print(bicycles)

# # Accessing elements
# print(bicycles[0])  # First element
# print(bicycles[1])  # Second element
# print(bicycles[3])  # Fourth element
# print(bicycles[-1]) # Last element

# # Modifying elements
# bicycles[0]='BMW'
# print(bicycles)

# # Adding elements
# bicycles.append('Honda')
# print(bicycles)

# # Inserting elements
# bicycles.insert(0,'Audi')
# print(bicycles)

# # Removing elements
# del bicycles[0]
# print(bicycles)

# # Using pop() to remove the last element
# popped_bicycle=bicycles.pop()
# print(bicycles)
# print(popped_bicycle)

# # adding message with the popped element
# message="My last bicycle was a " + popped_bicycle.title() + "."
# print(message)

# message1="My first bicycle was a " + bicycles[0].title() + "."
# print(message1)

# #project with lists, making a guest book

# guests =["hitler", "osama", "ghajini", "nazis", "white supremacists", "isis"]
# def guestss():
#     for i in guests:
#         message=f'hey {i},you are invited'
#         print(message)
#         print("this is print from function")


# # we just heard isis cannot join us for technical reasons

# declined_invitation=guests.remove('isis')
# print (guests)
# print("this is print from declined")
# guestss()

# #isis says we can invite alqayda instead

# guests.append('alqayda')
# guestss()

# #suddenly lots of people are calling us, its going to be a hit

# guests.insert(1,'hamas')
# guests.insert(4,'hezbollah')
# guests.append('isi')
# guestss()

# def remove_guests():
#     print(guests)
#     while len(guests) > 2:
#      removed_guest = guests.pop()   # removes the last guest
#      print(f"Sorry {removed_guest}, we can’t invite you to dinner.")
#     for guest in guests:
#         print(f"Hey {guest}, you’re still invited to dinner!")

# remove_guests()

# del guests[:]
# print(guests)

# .
# .
#2nd project with lists:

pizzas=['cheese','macaroni','pineapple','double crust']
print(pizzas)

for pizza in pizzas:
    print(f'i love {pizza.title()} so much')
    print(f'how much does {pizza.title()} cost')
print(f'wow they are so expensive')


for numbers in range(1,5):
    print(numbers)

numbers=list(range(1,5))
print(numbers)

print(numbers[0])

squares=[]

for numbers in range(1,11):
    square=numbers**2
    squares.append(square)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

for even in range(2,100,2):
    print(even)

even=list(range(2,100,2))
print(even)


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[-3:])
print(players[1:])
print(players[2:4])

#players[start:end:step]
#step/skip=2  skips one element each time

print(players[0:5:2])

#If you want to skip every other element in the whole list, just do:
print(players[::2])

#looping through the list
for i in players [0:3]:
    print(f'these are my first 3 players {i}')

#concept of copying lists

players=['ana','lucas','job']
villains=['kai','rabbit','longshadow']
players=villains[:]
print(players)
players.append('sugar')
print(players)
print(villains)


#trying deep copy and limitations


players=[['ana','lucas','job'],['1','2']]
copied_players=players.copy()
print(copied_players)

#so this right here is an example of shallow copy
#shallow copy essentially means that the list although would print out to be same
#however they are not independent, and one change in 1 list will do a similar change in copied list as well.
players[0].append('tony')
print(players)
print(copied_players)



#however if we use the slicing method to copy
print('using slicing method to copy')
players=copied_players[:]
print(players)
print(copied_players)
players[0].append('new')
print(players)
print(copied_players) #so i tried the earlier slicing method to copy, but this time change 
#to 1 list is doing a change to both lists, so it basically means that nested lists 
#can only be copied in true sense using the deepcopy method?


#using deepcopy

print('deepcopy starts here')
import copy
copied_players=copy.deepcopy(players)
players[0].append('deep')
print(players)
print(copied_players)
