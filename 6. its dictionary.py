# print("hey lets learn dictionary \n")

# #simple dictionary
# alien={'color':'green', 'point':5}
# print(alien['color'])
# print(alien['point'])


# #using values and pulling them in code.
# shot_alien=alien['color']
# earned_point=alien['point']
# print(f'you shot down {shot_alien} alien you earned {earned_point} points')


# alien['weapon']='gun'
# alien['celebration']='dance'
# print(alien)

# #A Dictionary of Similar Objects

# guys={
#     'john':'python',
#     'dow':'c++',
#     'cal':'java',
#     'sofi':'python'
# }
# print(guys)
# print(guys['john'])
# print(guys['c++']) #so here value retrieval isnt working

# Assigning a default value, if the corresponding key doesn't have a value assigned

# alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) # so if we run this till here, itll throw error since points isnt there in dict.

#however if we define a get method we explicitly set a key and value to give if no corresponding value is there in dict.
#if value is present in dict, that will be checked and fetched first, this default setting will come later.

# alien = {'color': 'green', 'speed': 'slow'}
# point_value = alien.get('points', 'No point value assigned.')
# print(point_value)

# here we will try to prove the same.

# alien = {'color': 'green', 'speed': 'slow','points':5}
# point_value = alien.get('points', 'No point value assigned.')
# weapon_value = alien.get('weapon', 'No weapon assigned.') #we cannot assign multiple defaults in single get
# print(point_value)
# print(weapon_value)

# #looping through the dictionary using items function:
# for a,b in alien.items():
#     print(f"did you see that alien it had {a} {b}")


guys={
    'john':'python',
    'dow':'c++',
    'cal':'java',
    'sofi':'python'
}

# bros={'john','sofi'}
# for names,languages in guys.items():
#     print(f"so the guys name is {names} and he codes in {languages}, how difficult is that")
#    # print(f"so if i had to just print values i'd just call {languages}\n")

#     if names in bros:
#         print(f"my man {names} loves {languages}")

#we are using keys method here, please note we are doing this outside loop so it doesnt print same message again
#we have done this with dictionary 'guys' itll work directly with dict and not with names variable of for loop.
# if 'erin' not in guys.keys():
#         print("erin please take the poll")

#lets print the keys sorted

# for names in sorted(guys.keys()):
#      print(names,"thank you for taking the poll!")

# #lets use and print the values sorted


for names in sorted(guys.values()):
     if names=='python':
          print(names,"nah thats not so tough")
     else:
          print(names,"thats a tough language")
     
     


        

