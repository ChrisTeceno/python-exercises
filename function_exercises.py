# Exercises
# Create a file named function_exercises.py for this exercise.
# After creating each function specified below, write the necessary code in
# order to test your function.

# Define a function named is_two.
# It should accept one input and
# return True if the passed input is either the number or the string 2,
# False otherwise.
def is_two(n):
    "returns true or false if input is a 2 or '2'"
    # check if 2 or '2'
    return n == 2 or n == "2"


# test function
is_two("2")
is_two(2)
is_two(1)
# ************************************************************************

# Define a function named is_vowel.
# It should return True if the passed string is a vowel, False otherwise.
def is_vowel(n):
    "returns true or false if input is a vowel"
    return n.lower() in ("a", "e", "i", "o", "u")


# test
is_vowel("a")
is_vowel("A")
is_vowel("b")

# ************************************************************************

# Define a function named is_consonant.
# It should return True if the passed string is a consonant,
# False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(n):
    "returns true or false if input is consonant"
    # is a letter and is the string only one char"
    if n.isalpha() and len(n) == 1:
        # check if its a vowel and flip boolean
        return not is_vowel(n)
    else:
        return False


# test
is_consonant("a")
is_consonant("ccc")
is_consonant("c")
is_consonant("1")

# ************************************************************************


# Define a function that accepts a string that is a word.
# The function should capitalize the first letter of the word
# if the word starts with a consonant.
def cap_first_consonant(n):
    """return the input string with a capital first letter 
    if the first letter is a consonant"""
    # is the first letter a consonant
    if is_consonant(n[0]):  
        # replace the first letter with uppercase
        return n.replace(n[0], n[0].upper(), 1)


# test cases
cap_first_consonant("test")
cap_first_consonant("apple")
cap_first_consonant("TEST")
# *************************************************************************

# Define a function named calculate_tip.
# It should accept a tip percentage (a number between 0 and 1)
# and the bill total, and return the amount to tip.
def calculate_tip(bill, tip):
    """return tip amount from entered bill and tip percent 
    bill in numeric form and tip 0.0 to 1.0 (100%) or higher"""
    # simple math
    return bill * tip

#test cases
calculate_tip(100, 0.25)
calculate_tip(1000, 0.2)
calculate_tip(100, 0.5)
# *************************************************************************

# Define a function named apply_discount.
# It should accept a original price, and a discount percentage,
# and return the price after the discount is applied.
def apply_discount(price, discount):
     """return price after discount, input """
    return price - (price * discount)

#test
apply_discount(100, 0.10)
# *************************************************************************

# Define a function named handle_commas.
# It should accept a string that is a number that contains commas
# in it as input, and return a number as output.
def handle_commas(number):
    """take a string of numbers and commas, remove commas"""
    #find all commas, replace with "" then return as float
    return float(number.replace(",", ""))

# test
handle_commas("1,000,000")
handle_commas("1,000,000.00000")
handle_commas("1000000")
# *************************************************************************


# Define a function named get_letter_grade.
# It should accept a number and return the letter grade associated with
# that number (A-F).
def get_letter_grade(grade):
    """take in int grade and return letter grade"""
    #check conditions and return once met
    if grade > 100:
        print("Someone did a lot of bonus problems!!!!")
        return("{} is an A++++++".format(grade))
    elif grade > 98:
        return("{} is an A+".format(grade))
    elif grade > 92:
        return("{} is an A".format(grade))
    elif grade > 88:
        return("{} is an A-".format(grade))
    elif grade > 85:
        return("{} is an B+".format(grade))
    elif grade > 81:
        return("{} is an B".format(grade))
    elif grade > 79:
        return("{} is an B-".format(grade))
    elif grade > 77:
        return("{} is an C+".format(grade))
    elif grade > 68:
        return("{} is an C".format(grade))
    elif grade > 66:
        return("{} is an C-".format(grade))
    elif grade > 64:
        return("{} is an D+".format(grade))
    elif grade > 61:
        return("{} is an D".format(grade))
    elif grade > 59:
        return("{} is an D-".format(grade))
    else:
        return("{} is an F---------".format(grade))


get_letter_grade(1000)
# *************************************************************************


# Define a function named remove_vowels
# that accepts a string and returns a string with all the vowels removed.
def remove_vowels(word):
    """input string, remove all vowels"""
    #loop through letter
    for letter in word:
        #if its a vowel
        if is_vowel(letter):
            #replace vowel with ""
            word = word.replace(letter, "")
    return word

#test
remove_vowels("word")
remove_vowels("words and other things 3424234")
remove_vowels("word up magazine!")
# *************************************************************************


# Define a function named normalize_name.
# It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed


def normalize_name(name):
    """take input, remove bad chars, leading/trailing
    white space and make lower"""
    # run through all letter and delete non valid chars
    for letter in name:
        #if its not a valid identifier
        if not letter.isidentifier():
            #but not a " "
            if letter != " ":
                # replace
                name = name.replace(letter, "")
    # strip and make lower
    name = name.strip().lower()
    # replace internal spaces with '_'
    name = name.replace(" ", "_")
    return name

#test
normalize_name(" stEVe Harvey#@$")
normalize_name("I eat a lot of tacos")
normalize_name("When IS LUNCH!@#!@#!")
normalize_name("Name") #will become name
normalize_name("First Name") #will become first_name
normalize_name("% Completed") #will become completed
# *************************************************************************


# Write a function named cumulative_sum
# that accepts a list of numbers and returns a list
# that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
def cumulative_sum(list):
    """take in a list, return a list with cumulative
     sums along the list"""
     # make a variable to track sum
    current_sum = 0
    #make a list to be outputted
    sum_list = []
    # got through input list
    for n in list:
        #increase sum
        current_sum += n
        #add new value to output list
        sum_list.append(current_sum)
        #return the new list
    return sum_list

# test
cumulative_sum([1, 1, 1])  # returns [1, 2, 3]
cumulative_sum([1, 2, 3, 4])  # returns [1, 3, 6, 10]
# *************************************************************************


# Additional Exercise
# Once you've completed the above exercises,
# follow the directions from
# https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886
# in order to thouroughly comment your code to explain your code.

# *************************************************************************


# Bonus
# Create a function named twelveto24.
# It should accept a string in the format 10:45am or 4:30pm
# and return a string that is the representation of the
# time in a 24-hour format. Bonus write a function that does the opposite.
def twelveto24(time12):
    """take in a time string 'HH:MMam/pm' return string as 'HHMM'
    corrected for 24 hour clock"""
    #split time into HH and MMam/pm
    time_bits = time12.split(':')
    #check if am in string
    if "am" in time12.lower():
        #check time_bits[0] to see if single or double digit
        if len(time_bits[0])==1:
            #add leading 0 if its single digit
            time_bits[0]="0{}".format(time_bits[0])
        # set up variable with result
        #result is first bit of input plus the first 2 chars of second bit
        time24 = "{}{}".format(time_bits[0],time_bits[1][0:2])
        return(time24)
    #does not contain am so assume it is pm
    else:
        time24 = "{}{}".format(int(time_bits[0]) + 12,time_bits[1][0:2])
        return(time24)  

# test      
twelveto24('1:45am')
twelveto24('4:45pm')
twelveto24('11:45am')
twelveto24('10:45pm')
# *************************************************************************

def twentyfourto12(time24):
    """take in a time string 'HHMM' return string as 'HH:MMam/pm'
    corrected for 24 hour clock"""
    # single digit hour am
    if int(time24)<1000:
        # leading 0 not included in formatting
        return "{}:{}am".format(time24[-3],time24[-2:])
    #double digit hour am
    if int(time24)<1200:
        return "{}:{}am".format(time24[:-2],time24[-2:])
    #pm cases
    else:
        #input hour - 12
        new_hour= "{}".format((int(time24[-4:-2])-12))
        return "{}:{}pm".format(new_hour,time24[-2:])

# test      
twentyfourto12("0445")
twentyfourto12("1113")
twentyfourto12("1622")
twentyfourto12("2300")
# *************************************************************************

# Create a function named col_index.
# It should accept a spreadsheet column name,
# and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27

# import string to allow string.ascii_uppercase
import string

def col_index(col_name):
    """inout column name, return index, from A to ZZ"""
    #make list A-Z
    col_names = list (string.ascii_uppercase)
    # add AA-ZZ
    for i in range(26):
        #append i twice, A becomes AA
        col_names.append(col_names[i]*2)
    # run through know length A to ZZ
    for i in range(52):
        # check the col name vs current col name in index
        if col_names[i] == col_name:
            # return index plus  for offset, index starts at 0 not 1
            return i+1

# test
col_index('A') #returns 1
col_index('B') #returns 2
col_index('AA') #returns 27