# Scope refers to where a variable or function name is available to be used. For example, when we create variables in a function (such as by giving names to our parameters), that data is not available outside of that function.
# Variables defined inside a function are not accessible outside of it 

# def get_max_health(modifier, level):
#     return modifier * level

# my_modifier = 5
# my_level = 10

# max_health = get_max_health(modifier, level)
# print(max_health);

# max_health = get_max_health(my_modifier, my_level)
# print(max_health);



# So far we've been working in the global scope. That means that when we define a variable or a function, that name is accessible in every other place in our program, even within other functions.
# For example
# pi = 3.14

# def get_area_of_circle(radius):
#     return pi * radius * radius

# area_of_circle = get_area_of_circle(10)
# print(area_of_circle, "area of circle");
# Because pi was declared in the parent "global" scope, it is usable within the get_area_of_circle() function.
