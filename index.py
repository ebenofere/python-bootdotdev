# function to define the area of a circle
# def area_of_circle(r):
#     pi = 3.14
#     area = pi * r * r
#     return area

# radius = 7
# area = area_of_circle(radius)
# print(area)



# A function can return more than one value by separating them with commas.
# def cast_iceblast(wizard_level, start_mana):
#     damage = wizard_level * 2
#     new_mana = start_mana - 10
#     return damage, new_mana # return two values

# print(cast_iceblast (5, 17));



# When calling a function that returns multiple values, you can assign them to multiple variables.
# dmg, mana = cast_iceblast(5, 100)
# print(f"Damage: {dmg}, Remaining Mana: {mana}")
# Damage: 10, Remaining Mana: 90

# When cast_iceblast is called, it returns two values. The first value is assigned to dmg, and the second value is assigned to mana. Just like function inputs, it's the order of the values that matters, not the variable names. We could just as easily called the variables one and two:

# The damage and new_mana variables from cast_iceblast's function body only exist inside of the function. They can't be used outside of the function. We'll explain that more later when we talk about scope.



def become_warrior(full_name, power):
    title = f"{full_name} aka 'The Beast'"
    new_power = power + 1
    return title, new_power

name, strength = become_warrior("Obafemi Martins", 98);
print(f"One of the best strikers in the Italian League back in the early 2000s was {name}.\nHis strength on PlayStation 1 was {strength}")
