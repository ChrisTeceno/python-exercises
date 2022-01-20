# # Exercises
# # Do your work for this exercise in a file named
# # control_structures_exercises.py.

# Conditional Basics

# prompt the user for a day of the week, print out whether the day
#  is Monday or not


from turtle import title


is_monday = "monday" == input("Name a day of the week\n").lower()
print("Your response is monday?")
print(is_monday)


# *******************************************************************
# prompt the user for a day of the week, print out whether the day
#  is a weekday or a weekend
is_weekday = input("Name a day of the week\n").lower() in (
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
)
print("Your response is a weekday?")
print(is_weekday)

# *******************************************************************
# create variables and make up values for

# the number of hours worked in one week
hours_worked = 30
# the hourly rate
hourly_rate = 160
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck.
# You get paid time and a half if you work more than 40 hours
weekly_pay = 0
if hours_worked <= 40:
    print("The man is not happy! WORK MORE!\nPre-tax pay is:")
    weekly_pay = hours_worked * hourly_rate
else:
    print("Congratulations on working extra for the man!\nPre-tax pay is:")
    weekly_pay = 40 * hourly_rate
    weekly_pay += hours_worked % 40 * hourly_rate * 1.5
print(weekly_pay)

# *******************************************************************
# Loop Basics

# While

# Create an integer variable i with a value of 5.
i = 5
# Create a while loop that runs so long as i is less than or
# equal to 15
while i <= 15:
    # Each loop iteration, output the current value of i, then
    print(i)
    # increment i by one.
    i += 1
# Your output should look like this:


# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15

i = 5
while i <= 15:
    print(i)
    i += 1

# *******************************************************************

# Create a while loop that will count by 2's starting with
# 0 and ending at 100. Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    print("\n")
    i += 2
# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5

# Create a while loop that starts at 2, and displays the number
# squared on each line while the number is less than 1,000,000.
i = 2
while i <= 1000000:
    print(i)
    i = i * i

# Output should equal:

#  2
#  4
#  16
#  256
#  65536

# *******************************************************************

# Write a loop that uses print to create the output shown below.
i = 100
while i >= 5:
    print(i)
    i -= 5
# 100
# 95
# 90
# 85
# 80
# 75
# 70
# 65
# 60
# 55
# 50
# 45
# 40
# 35
# 30
# 25
# 20
# 15
# 10
# 5


# *******************************************************************
# For Loops

# Write some code that prompts the user for a number, then shows
# a multiplication table up through 10 for that number.

# For example, if the user enters 7, your program should output:

user_number5 = ""
while user_number5.isdigit() == False:
    user_number5 = input("What number would you like to multiple by?\n")
multiple = int(user_number5)
for i in range(1, 11):
    print("{} x {} = {}".format(multiple, i, multiple * i))

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70


# *******************************************************************

# Create a for loop that uses print to create the output shown
# below.
for i in range(10):
    print(str(i) * i)

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
# break and continue

# Prompt the user for an odd number between 1 and 50. Use a loop
#  and a break statement to continue prompting the user if they
#  enter invalid input. (Hint: use the isdigit method on strings
#  to determine this). Use a loop and the continue statement to
#  output all the odd numbers between 1 and 50, except for the
#  number the user entered.


i = 1
while True:
    user_number = input("Please enter a ODD NUMBER between 0 and 50")
    if user_number.isdigit() == True:
        if int(user_number) % 2 == 1:
            skip_number = int(user_number)
            break

print("Number to skip is {}\n".format(skip_number))

i = 1
while i < 50:
    if i != skip_number:
        print("Here is an odd number: {}".format(i))
    else:
        print("Yikes! Skipping number: {}".format(i))
    i += 2
# Your output should look like this:

# Number to skip is: 27

# Here is an odd number: 1
# Here is an odd number: 3
# Here is an odd number: 5
# Here is an odd number: 7
# Here is an odd number: 9
# Here is an odd number: 11
# Here is an odd number: 13
# Here is an odd number: 15
# Here is an odd number: 17
# Here is an odd number: 19
# Here is an odd number: 21
# Here is an odd number: 23
# Here is an odd number: 25
# Yikes! Skipping number: 27
# Here is an odd number: 29
# Here is an odd number: 31
# Here is an odd number: 33
# Here is an odd number: 35
# Here is an odd number: 37
# Here is an odd number: 39
# Here is an odd number: 41
# Here is an odd number: 43
# Here is an odd number: 45
# Here is an odd number: 47
# Here is an odd number: 49

# *******************************************************************

# The input function can be used to prompt for input and use that
# input in your python code. Prompt the user to enter a positive
# number and write a loop that counts from 0 to that number.
# (Hints: first make sure that the value the user entered is a
# valid number, also note that the input function returns a string,
# so you'll need to convert this to a numeric type.)

# initialize string and int for input while loop
user_number2 = ""
to_number = 1

# loop until proper input given (even int)
while to_number % 2 != 0:  # is even
    user_number2 = input("Please enter an EVEN NUMBER")
    if user_number2.isdigit():  # was the input a digit
        to_number = int(user_number2)

i = 0
while i <= to_number:
    print(i)
    i += 1

# *******************************************************************

# Write a program that prompts the user for a positive integer.
#  Next write a loop that prints out the numbers from the number
#  the user entered down to 1.

# initialize string and int for input while loop
user_number3 = ""
from_number = 1

# loop until proper input given (even int)
while from_number % 2 != 0:  # is even
    user_number3 = input("Please enter an EVEN NUMBER")
    if user_number3.isdigit():  # was the input a digit
        from_number = int(user_number3)

i = from_number
while i >= 1:
    print(i)
    i -= 1


# *******************************************************************

# Fizzbuzz

# One of the most common interview questions for entry-level
# programmers is the FizzBuzz test. Developed by Imran Ghory,
# the test is designed to test basic looping and conditional
# logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print
# "FizzBuzz".

for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

# *******************************************************************

# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
# initialize string and int for input while loop
user_number4 = ""
while user_number4.isdigit() == False:
    user_number4 = input("What number would you like to go up to?\n")
to_number2 = int(user_number4)
print("Here is your table! \n")
print("number | squared | cubed")
print("------ | ------- | -----")
for i in range(1, to_number2 + 1):
    if input("would you like to continue? (y or n") == "n":
        break
    print("{:<7}| {:<8}| {:<7}".format(i, i ** 2, i ** 3))
    i += 1

# Example Output

# What number would you like to go up to? 5

# Here is your table!

# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125
# Bonus: Research python's format string specifiers to align the
# table

# *******************************************************************

# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0
# Bonus

# Edit your grade ranges to include pluses and minuses
# (ex: 99-100 = A+).


def convert_grades():
    user_number6 = input(
        "Insert a number (0-100) to get a letter grade?\nInsert a letter to stop"
    )
    grade = int(user_number6)
    while user_number6.isdigit():
        if grade > 100:
            print("{} is an A++++++".format(grade))
            print("Someone did a lot of bonus problems!!!!")
        elif grade > 98:
            print("{} is an A+".format(grade))
        elif grade > 92:
            print("{} is an A".format(grade))
        elif grade > 88:
            print("{} is an A-".format(grade))
        elif grade > 85:
            print("{} is an B+".format(grade))
        elif grade > 81:
            print("{} is an B".format(grade))
        elif grade > 79:
            print("{} is an B-".format(grade))
        elif grade > 77:
            print("{} is an C+".format(grade))
        elif grade > 68:
            print("{} is an C".format(grade))
        elif grade > 66:
            print("{} is an C-".format(grade))
        elif grade > 64:
            print("{} is an D+".format(grade))
        elif grade > 61:
            print("{} is an D".format(grade))
        elif grade > 59:
            print("{} is an D-".format(grade))
        else:
            print("{} is an F---------".format(grade))
        # get next number or abort
        user_number6 = input(
            "Insert a number (0-100) to get a letter grade?\n"
            + "Insert a letter to stop"
        )
        if user_number6.isdigit():
            grade = int(user_number6)
        else:
            print("Grades complete")
            break


# run the function
convert_grades()
# *******************************************************************

# Create a list of dictionaries where each dictionary represents a
# book that you have read. Each dictionary in the list should have
# the keys title, author, and genre. Loop through the list and
# print out information about each book.

# Prompt the user to enter a genre, then loop through your books
# list and print out the titles of all the books in that genre.

books_read = []
books_read.append({"title": "Tribe", "author": "Junger", "genre": "Non-Fiction"})
books_read.append({"title": "Sapiens", "author": "Harari", "genre": "Non-Fiction"})
books_read.append({"title": "Rationality", "author": "Pinker", "genre": "Non-Fiction"})
books_read.append({"title": "1984", "author": "Orwell", "genre": "Dystopian Fiction"})
for book in books_read:
    print(book)

genre = input("pick a genre (i.e. 'non-fiction')").lower()
for book in books_read:
    if book["genre"].lower() == genre:
        print(book["title"])
