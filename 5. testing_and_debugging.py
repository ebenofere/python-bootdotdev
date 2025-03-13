# A unit test is just an automated program that tests a small "unit" of code. Usually just a function or two. The editor will have tabs: the "main.py" file containing your code, and the "main_test.py" file containing the unit tests.

# These new unit-test-style lessons will test your code's functionality rather than its output. Our tests will call functions in your code with different arguments, and expect certain return values. If your code returns the correct values, you pass. If it doesn't, you fail.

# There are two reasons for this change:
# 1. It's more realistic. In the real world, you'll be writing unit tests and running them against your code to make sure it works as expected.
# 2. You can run and debug your code with print statements, and leave those print statements in when you submit. Unlike the output-based lessons, you won't have to remove your print statements to pass.

# The pass keyword is a way to tell Python to do nothing. You'll need to replace it with your own code.


def total_xp(level, xp_to_add):
    level_weight = 100
    total_xp = level * level_weight + xp_to_add
    return total_xp