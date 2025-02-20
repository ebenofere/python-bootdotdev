# function to define the area of a circle
# def area_of_circle(r):
#     pi = 3.14
#     area = pi * r * r
#     return area

# radius = 7
# area = area_of_circle(radius)
# print(area)



# A function can return more than one value by separating them with commas.
def cast_iceblast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana # return two values

# print(cast_iceblast (5, 17));



# When calling a function that returns multiple values, you can assign them to multiple variables.
dmg, mana = cast_iceblast(5, 100)
print(f"Damage: {dmg}, Remaining Mana: {mana}")
# Damage: 10, Remaining Mana: 90
# When cast_iceblast is called, it returns two values. The first value is assigned to dmg, and the second value is assigned to mana. Just like function inputs, it's the order of the values that matters, not the variable names. We could just as easily called the variables one and two:

