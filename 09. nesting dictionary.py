# #simple nesting example
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens=[alien_0,alien_1,alien_2]

# for alien in aliens:
#     print(alien)

# # please note that even if items are same, they will all be considered separate unique items by python

# aliens=[]

# for ali in range(30):
#     newalien={'color': 'green', 'points': 5}
#     aliens.append(newalien)

# for alien in aliens[:5]:
#     print(alien)

# print(len(aliens))

# # how about we change the first 3 aliens into a little fast moving yellow aliens.

# for alien in aliens[:3]:
#     if alien['color']=='green':
#         alien['color']='yellow'
#         alien['points']=10
#         alien['speed']='medium'
#     print(alien)

# for alien in aliens[:6]:
#     print(alien)

# # A List in a Dictionary
# pizza={
#     "crust":"thick", "toppings":["cheese","macaroni","mushroom"]
# }

# #trying different ways to print and get output
# print(f"so you ordered pizza with {pizza['crust']} crust and chose toppings: {pizza['toppings']}")
# print(f"so you ordered pizza with {pizza['crust']} crust and chose toppings: {', '.join(pizza['toppings'])}")

# print(f"You ordered a {pizza['crust']}-crust pizza "
#  "with the following toppings:")

# for topping in pizza['toppings']:
#   print("\t" + topping)

# # trying nesting multiple lists in dictionary

# languez={
#     "jen":["python","c","java"],
#     "sofi":["c"],
#     "avi":["java","ruby","python"]
# }
# for name, lang in languez.items():
#     print(f"so {name}'s favorite languages are: {lang}") #this is common way to get lang items
#     for langi in lang: #this is more refined way to do it
#         print(f"{langi}")

# # a dictionary in dictionary

# users={
#     "asingh":{
#         "first":"abhi", "last":"singh","location":"ind"
#     },
#     "bsingh":{
#         "first":"bikas","last":"singh","location":"us"
#     }
# }

# for uname,uinfo in users.items():
#     print(f"{uname}")
#     una=(f"username is {uname} and first name is {uinfo['first']}, and last name is {uinfo['last']}")
#     loc=uinfo["location"]

#     print(f"{una.title()}")    
#     print(f"location is {loc.title()}")


    #practice nesting

countr={
        "india":{
            "state":"up","cm":"yogi", "state":"assam", "cm":"himanta"
        },
        "amrika":{
            "state":"mexico","cm":"sopra", "state":"penni", "cm":"nopra"
        }
    }

for sc,st in countr.items():
        print(f"country {sc}")
        state=(f"{st['state']} in country {sc} has cm {st['cm']}")
        print(f"{state}")

#draft 2

countr = {
    "india": [
        {"state": "up", "cm": "yogi"},
        {"state": "assam", "cm": "himanta"}
    ],
    "amrika": [
        {"state": "mexico", "cm": "sopra"},
        {"state": "penni", "cm": "nopra"}
    ]
}

for country, states in countr.items():
    print(f"\nCountry: {country.title()}")
    for info in states:
        print(f"  State: {info['state'].title()} | CM: {info['cm'].title()}")


# mini practice

employee = {
    'name': 'John',
    'details': {
        'role': 'Developer',
        'city': 'Delhi'
    }
}

print(employee.get('name', 'No name'))
print(employee.get('details', {}).get('role', 'No role'))
print(employee.get('details', {}).get('salary', 'No salary info'))

# mini practice to use get() method


users={
    "asingh":{
        "first":"abhi", "last":"singh","location":"ind"
    },
    "bsingh":{
        "first":"bikas","last":"singh","location":"us"
    }
}

for username,info in users.items():
     print(f"username: {username}")
     print(f"first name: {info.get('first','n/a')}")
     print(f"last name: {info.get('last','n/a')}")
     print(f"location: {info.get('location','n/a')}")


# taking user input and filling up a dictionary step by step

# 1. Simple Dictionary (single key-value)

person = {}  # empty dictionary

name = input("Enter your name: ")
age = input("Enter your age: ")

person['name'] = name
person['age'] = age

print("Here’s your data:", person)

# 2. Multiple entries (loop)

users = {}

while True:
    username = input("Enter a username (or 'done' to quit): ").strip()
    if username.lower() == 'done':
        break

    age = input(f"Enter {username}'s age: ").strip()
    users[username] = age

print("\nAll users:", users)

# Nested dictionary (one user → multiple fields)

users = {}

while True:
    username = input("Enter a username (or 'done' to quit): ").strip()
    if username.lower() == 'done':
        break

    age = input("Enter age: ").strip()
    city = input("Enter city: ").strip()
    hobby = input("Enter hobby: ").strip()

    # store all user info in a nested dictionary
    users[username] = {
        'age': age,
        'city': city,
        'hobby': hobby
    }

print("\nFinal data:")
for user, info in users.items():
    print(f"{user.title()}: {info}")


# Nested list inside dictionary (user with multiple hobbies)

users = {}

username = input("Enter your name: ")
age = input("Enter your age: ")

hobbies = []
while True:
    hobby = input("Enter a hobby (type 'ok' when done): ").strip()
    if hobby.lower() == 'ok':
        break
    hobbies.append(hobby)

users[username] = {
    'age': age,
    'hobbies': hobbies
}

print("\nUser details:")
for name, info in users.items():
    print(f"{name.title()} → Age: {info['age']}, Hobbies: {', '.join(info['hobbies'])}")



