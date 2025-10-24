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
print("you choose: " ,choice_list)
total1=0
top=input(f"{name}, would you also like to add some toppings, say 'y' or 'n: ")
if top=='y':
   print("we have butter, ghee, cheese as toppings ")
   top_choice=input("please choose toppings: ")
   top_list=top_choice.split(',')
   top_list=[k.strip() for k in top_choice.split(',')]
   print("you choose: " ,top_list,"as toppings")
   
   for c in top_list:
      if c in toppings:
         print(f"{c} is available at {toppings[c]} rupeess")
         total1+=toppings[c]
      else:
         print(f"{c} this isnt available")

elif top=='n':
   print("ok no problem, enjoy plain order")
else:
   print("wrong choice, try again")
total = 0   # initialize before the loop
for a in choice_list:
    if a in menu:
     print (f"{a} is available at {menu[a]}")
     total += menu[a]    # only add price if available
    else:
       print(f"{a} this isnt available")

grand=total1+total
print(f"\nYour total bill is ₹{grand}")
print(f"{name}, thank you for eating with us")

#darft 2 turned out better than expectation, its already a functioning project

