#hear me out
# am making a cafe
# we will use everything we have learnt till now
# print("------------------------gabru cafe-------------------------")

# name=input("enter name of visiting customer: ")
# print(f"welcome {name} to gabru pizza, please have a look at the menu")
# print("we have--> pizza, dal, naan, paronthe")
# menu={'pizza':350,'dal':100,'naan':30,'paronthe':35}
# toppings={'butter':20,'ghee':30,'cheese':25}
# ch=input("i'd like to have: ")
# print ("do you want any toppings with your order? ")
# print("check menu --> butter, ghee, cheese")
# nm=input("i'd like to have: ")

# for a,b in menu.items():
#     if a==ch:
#         print(f"so youll have {a}, itll cost you {b}")
#         break;
# else:
#     print("this isnt available")
# for c,d in toppings.items():
#     if c==nm:
#         print(f"so youll have {c}, itll cost you {d}")

#         total=b+d
#         print("your total is:",total)

# draft 2

print("------------------------gabru cafe-------------------------")

name=input("enter name of visiting customer: ")
print(f"welcome {name} to gabru pizza, please have a look at the menu")
print("we have--> pizza, dal, naan, paronthe")
menu={'pizza':350,'dal':100,'naan':30,'paronthe':35}
toppings={'butter':20,'ghee':30,'cheese':25}
choice=input("i'd like to have: ")
choice_list=choice.split(',')
choice_list=[t.strip() for t in choice.split(',')]  
print(choice_list)