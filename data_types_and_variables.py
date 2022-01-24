# Create a Python script file named data_types_and_variables.py. Inside it, write some
# Python code, that is, variables and operators, to describe the following scenarios.
#  Do not worry about the real operations to get the values,
# the goal of these exercises is to understand how real world conditions can be
# represented with code.

#  You have rented some movies for your kids: The little mermaid (for 3 days),
#  Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know
# yet if they're going to like it). If price for a movie per day is 3 dollars,
#  how much will you have to pay?

the_little_mermaid = 3
brother_bear = 5
hercules = 1
total_days = the_little_mermaid + brother_bear + hercules
total_payment = total_days * 3
print("The total payment for these movies is: {}".format(total_payment))

# *******************************************************************************


# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook,
# they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380,
#  and Facebook 350. How much will you receive in payment for this week? You worked 10
#  hours for Facebook, 6 hours for Google and 4 hours for Amazon.


def weekly_pay():
    hours_google = int(input("how many hours did you work for google?\n"))
    hours_amazon = int(input("how many hours did you work for amazon?\n"))
    hours_facebook = int(input("how many hours did you work for facebook?\n"))
    weekly_pay = 400 * hours_google + 380 * hours_amazon + 350 * hours_facebook
    return "Your weekly pay is: {}".format(weekly_pay)


print(weekly_pay())

# Inputs: google 6, amazon 4, facebook 10
# Your weekly pay is: 7420
# *******************************************************************************


# A student can be enrolled to a class only if the class is not full and the class
# schedule does not conflict with her current schedule.


def can_enroll():
    is_full = input("Is the class full? True or False?\n")
    class_conflict = input("is there a class conflict? True or False?\n")
    can_enroll = (is_full.lower() != "true") and (class_conflict.lower() != "true")
    if can_enroll:
        return "Student can enroll"
    else:
        return "Student can NOT enroll"


# test funtion
print(can_enroll())

# both not true
# can enroll var = True
# Student can enroll

# is_full true
# can enroll var = False
# Student can NOT enroll

# class_conflict true
# can enroll var = False
# Student can NOT enroll

# is_full true and class_conflict true
# can enroll var = False
# Student can NOT enroll
# ******************************************************************************


# A product offer can be applied only if people buys more than 2 items,
# and the offer has not expired. Premium members do not need to buy a specific amount
#  of products.

total_items = int(input("How many items are bought:\n"))
is_expired = input("Is offer expired? True or False.\n").lower() == "true"
is_premium = input("Is member premium? True or False.\n").lower() == "true"
can_apply = (is_premium and not is_expired) or (total_items > 2 and (not is_expired))


# Continue working in your data_types_and_variables.py file. Use the following
#  code to follow the instructions below:

username = "codeup"
password = "notastrongpassword"
# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
password_long_enough = len(password) >= 5
# the username must be no more than 20 characters
username_short_enough = len(username) <= 20
# the password must not be the same as the username
username_password_unique = username != password
# bonus neither the username or password can start or end with whitespace
no_whitespace = " " not in (username + password)

# BONUS
# For practicing with list comprehensions, work through 17 List Comprehension Exercises.
# Add your solutions to a new file named list_comprehensions.py

# For even more practice with all your Python tools together,
# work through 20 Python Data Structure Manipulation Exercises.
# Name this file python_data_structure_manipulation_exercises.py.
