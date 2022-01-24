# Exercises
# You will need to use imports to complete each exercise; in addition,
# these exercise will strengthen your problem solving and python coding
# skills.

# You will be directed to create specific files in part 1, for the rest
# you may do your work in either import_exercises.py or import_exercises.
# ipynb.

# Import and test 3 of the functions from your functions exercise file.
# Import each function in a different way:

# Run an interactive python session and import the module. Call the
# is_vowel function using the . syntax.

# In [8]: import function_exercises as fe

# In [9]: fe.is_vowel('a')
# Out[9]: True

# In [10]: fe.is_vowel('b')
# Out[10]: False

# Create a file named import_exericses.py. Within this file, use from to
# import the calculate_tip function directly. Call this function with
# values you choose and print the result.

from function_exercises import calculate_tip

print(calculate_tip(100))
print(calculate_tip(100, 0.25))
print(calculate_tip(375.67, 0.21))
# Create a jupyter notebook named import_exercises.ipynb. Use from to
# import the get_letter_grade function and give it an alias. Test this
# function in your notebook.
# Make sure your code that tests the function imports is run from the
# same directory that your functions exercise file is in.

# Read about and use the itertools module from the python standard library
# to help you solve the following problems:
import itertools as it

# How many different ways can you combine the letters from "abc" with the
# numbers 1, 2, and 3?
combos = []
for i in range(1, 7):
    combos.extend(list(it.combinations("abc123", i)))
print(len(combos))  # 63 combos of different lengths
print(len(list(it.permutations("abc123"))))  # 720 permutations

# How many different combinations are there of 2 letters from "abcd"?
print(len(list(it.combinations("abcd", 2))))  # 6

# How many different permutations are there of 2 letters from "abcd"?
print(len(list(it.permutations("abcd", 2))))  # 12

# Save this file as profiles.json inside of your exercises directory
# (right click -> save file as...).

# Use the load function from the json module to open this file.


# import json

# json.load
# Your code should produce a list of dictionaries. Using this data,
# write some code that calculates and outputs the following information:
import json

profiles = json.load(open("profiles.json"))
print(profiles)

# Total number of users
print(len(profiles))  # 19

# Number of active users
count = 0
for user in profiles:
    if user["isActive"]:
        count += 1
print(count)  # 9

# Number of inactive users
count = 0
for user in profiles:
    if not user["isActive"]:
        count += 1
print(count)  # 10

# Grand total of balances for all users
grand_total = 0
for user in profiles:
    # remove $ and ','s then convert to float
    grand_total += float(user["balance"].replace("$", "").replace(",", ""))
print(grand_total)  # 52667.02

# Average balance per user
print(f"{grand_total/len(profiles):.02f}")  # 2771.95
# User with the lowest balance
lowest_balance = 10000000000
user_w_lowest_balance = ""
for user in profiles:
    user_balance = float(user["balance"].replace("$", "").replace(",", ""))
    if user_balance < lowest_balance:
        lowest_balance = user_balance
        user_w_lowest_balance = user["name"]
print(f"{user_w_lowest_balance} with {lowest_balance}")
# Avery Flynn with 1214.10

# User with the highest balance
highest_balance = 0
user_w_highest_balance = ""
for user in profiles:
    user_balance = float(user["balance"].replace("$", "").replace(",", ""))
    if user_balance > highest_balance:
        highest_balance = user_balance
        user_w_highest_balance = user["name"]
print(f"{user_w_highest_balance} with {highest_balance}")
# Fay Hammond with 3919.64

# Most common favorite fruit
fruits = {}
for user in profiles:
    if user["favoriteFruit"] not in fruits:
        fruits[user["favoriteFruit"]] = 1
    else:
        fruits[user["favoriteFruit"]] += 1
fruits_sorted = sorted(fruits.items(), key=lambda x: x[1], reverse=True)
print(fruits_sorted[0][1])
print(
    f"The most popular fruit is {fruits_sorted[0][0]}"
    + f" with {fruits_sorted[0][1]} people listing it"
)

# reference total counts
for fruit, count in fruits.items():
    print(f"There are {count} people listing {fruit}s" + " as their favorite")

# Least most common favorite fruit
print(
    f"""    The least popular fruit is {fruits_sorted[-1][0]} 
    with {fruits_sorted[-1][1]} people listing it"""
)

# Total number of unread messages for all users
unread_message_count = 0
for user in profiles:
    # the greeting message is uniform from the right
    # therefore you can pull the 2 digits by reverse index
    user_string_count = user["greeting"][-19:-17]
    unread_message_count += int(user_string_count)
print(unread_message_count)  # 210
