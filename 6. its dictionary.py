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

alien = {'color': 'green', 'speed': 'slow'}
point_value = alien.get('points', 'No point value assigned.')
print(point_value)

# here we will try to prove the same.

alien = {'color': 'green', 'speed': 'slow','points':5}
point_value = alien.get('points', 'No point value assigned.')
weapon_value = alien.get('weapon', 'No weapon assigned.') #we cannot assign multiple defaults in single get
print(point_value)
print(weapon_value)