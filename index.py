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



# def become_warrior(full_name, power):
#     title = f"{full_name} aka 'The Beast'"
#     new_power = power + 1
#     return title, new_power

# name, strength = become_warrior("Obafemi Martins", 98);
# print(f"One of the best strikers in the Italian League back in the early 2000s was {name}.\nHis strength on PlayStation 1 was {strength}")



# In Python you can specify a default value for a function argument. It's nice for when a function has arguments that are "optional". You as the function definer can specify a specific default value in case the caller doesn't provide one.
# A default value is created by using the assignment (=) operator in the function signature.

def get_greeting(name, email, age="32"):
    print(f"My name is {name}, I am {age} years old and my email is {email}")

print(get_greeting("Sam Altman", "saltman@openai.com", 39))
print(get_greeting("Eben Ofere", "eofere@openai.com"));

# If the second parameter is omitted, the default "there" value will be used in its place. As you may have guessed, for this structure to work, optional arguments (the ones with defaults) must come after all required arguments.

