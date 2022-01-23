# 20 Python Data Structure Manipulation Exercises
# The following questions reference the students data structure below. Write the python code to answer the following questions:


from audioop import reverse


students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]


# How many students are there?
print(len(students))

# How many students prefer light coffee? For each type of coffee roast?
light_count = 0
medium_count = 0
dark_count = 0
for student in students:
    if student["coffee_preference"] == "light":
        light_count += 1
    elif student["coffee_preference"] == "medium":
        medium_count += 1
    elif student["coffee_preference"] == "dark":
        dark_count += 1
print(f"{light_count} student(s) like light")
print(f"{medium_count} student(s) like medium")
print(f"{dark_count} student(s) like dark")

# How many types of each pet are there?
####### NOT SURE WHAT IS MEANT BY "types" so made a count of each pet
pets = {}
for student in students:
    # print(student)
    if student["pets"] != []:
        # print (student['pets'])
        for pet in student["pets"]:
            # print(pet)
            if pet["species"] not in pets:
                pets[pet["species"]] = 1
            else:
                pets[pet["species"]] += 1
for pet, count in pets.items():
    print(f"There are {count} {pet}s")

# How many grades does each student have? Do they all have the same number of grades? ### 4 AND YES
for student in students:
    print(student["student"], " has ", len(student["grades"]), " grades")

# What is each student's grade average?
for student in students:
    print(
        student["student"],
        " has ",
        sum(student["grades"]) / len(student["grades"]),
        " average grade",
    )

# How many pets does each student have?
for student in students:
    print(student["student"], " has ", len(student["pets"]), " pet(s)")

# How many students are in web development? data science?
web_development = 0
data_science = 0
for student in students:
    if student["course"] == "web development":
        web_development += 1
    else:
        data_science += 1
print(
    f"there are {web_development} web development students and",
    f"there are {data_science} data science students",
)

# What is the average number of pets for students in web development?
pet_count = 0
for student in students:
    if student["course"] == "web development":
        pet_count += len(student["pets"])
avg_pets = pet_count / 7
print(f"Web development students have an avg of {avg_pets:.2f} pets")

# What is the average pet age for students in data science?
pet_count = 0
total_age = 0
for student in students:
    if student["course"] == "data science" and len(student["pets"]) > 0:
        pet_count += len(student["pets"])
        for pet in student["pets"]:
            total_age += pet["age"]
avg_age = total_age / pet_count
print(f"The average pet age for students in data science is : {avg_age:.2f}")
# What is most frequent coffee preference for data science students?
light_count = 0
medium_count = 0
dark_count = 0
for student in students:
    if student["course"] == "data science":
        if student["coffee_preference"] == "light":
            light_count += 1
        elif student["coffee_preference"] == "medium":
            medium_count += 1
        elif student["coffee_preference"] == "dark":
            dark_count += 1
if light_count > medium_count and light_count > dark_count:
    print(f"Light coffee is the most frequent preference with {light_count} drinkers")
elif medium_count > dark_count:
    print(f"Medium coffee is the most frequent preference with {medium_count} drinkers")
else:
    print(f"Dark coffee is the most frequent preference with {dark_count} drinkers")
print(f"{light_count} data science student(s) like light")
print(f"{medium_count} data science student(s) like medium")
print(f"{dark_count} data science student(s) like dark")

# What is the least frequent coffee preference for web development students?
light_count = 0
medium_count = 0
dark_count = 0
for student in students:
    if student["course"] == "web development":
        if student["coffee_preference"] == "light":
            light_count += 1
        elif student["coffee_preference"] == "medium":
            medium_count += 1
        elif student["coffee_preference"] == "dark":
            dark_count += 1
if light_count < medium_count and light_count < dark_count:
    print(f"Light coffee is the least frequent preference with {light_count} drinkers")
elif medium_count < dark_count and medium_count < light_count:
    print(
        f"Medium coffee is the least frequent preference with {medium_count} drinkers"
    )
elif dark_count < medium_count and dark_count < light_count:
    print(f"Dark coffee is the least frequent preference with {dark_count} drinkers")
else:  # tie
    if light_count < medium_count:
        print(
            f"Dark and light coffee are tied for least frequent preference with {dark_count} drinkers each"
        )
    elif medium_count < dark_count:
        print(
            f"Medium and light coffee are tied for least frequent preference with {light_count} drinkers each"
        )
    elif dark_count < light_count:
        print(
            f"Dark and medium coffee are tied for least frequent preference with {dark_count} drinkers each"
        )

print(f"{light_count} web development student(s) like light")
print(f"{medium_count} web development student(s) like medium")
print(f"{dark_count} web development student(s) like dark")

# What is the average grade for students with at least 2 pets? 81.5
student_count = 0
grade_total = 0
for student in students:
    if len(student["pets"]) > 2:
        student_count += 1
        grade_total += sum(student["grades"])
avg_grade = grade_total / (student_count * 4)
print(f"The average grade for students with at least 2 pets is: {avg_grade:.2f}")

# What is the average grade for ALL students? 82.93
student_count = 0
grade_total = 0
for student in students:
    student_count += 1
    grade_total += sum(student["grades"])
avg_grade = grade_total / (student_count * 4)
print(f"The average grade for  all students is: {avg_grade:.2f}")

# How many students have 3 pets?
student_count = 0
for student in students:
    if len(student["pets"]) == 3:
        student_count += 1
print(f"{student_count} student(s) have 3 pets.")

# What is the average grade for students with 0 pets?
student_count = 0
grade_total = 0
for student in students:
    if len(student["pets"]) == 0:
        student_count += 1
        grade_total += sum(student["grades"])
avg_grade = grade_total / (student_count * 4)
print(f"The average grade for students with 0 pets is: {avg_grade:.2f}")

# What is the average grade for web development students? data science students?
web_student_count = 0
web_grade_total = 0
ds_student_count = 0
ds_grade_total = 0
for student in students:
    if student["course"] == "web development":
        web_student_count += 1
        web_grade_total += sum(student["grades"])
    else:
        ds_student_count += 1
        ds_grade_total += sum(student["grades"])
web_avg_grade = web_grade_total / (web_student_count * 4)
ds_avg_grade = ds_grade_total / (ds_student_count * 4)
print(f"The average grade for web development students is: {web_avg_grade:.2f}")
print(f"The average grade for data science students is: {ds_avg_grade:.2f}")

# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
grade_list = []
for student in students:
    if student["coffee_preference"] == "dark":
        avg_grade = sum(student["grades"]) / len(student["grades"])
        grade_list.append(avg_grade)
grade_list.sort()
print(grade_list)
print(grade_list[0], grade_list[-1])
print(
    f"The average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers is: {grade_list[-1]:.2f}, {grade_list[0]:.2f}"
)

# What is the average number of pets for medium coffee drinkers?
pet_count = 0
student_count = 0
for student in students:
    if student["coffee_preference"] == "medium":
        pet_count += len(student["pets"])
        student_count += 1
avg_pets = pet_count / student_count
print(f"medium coffee drinking students have an avg of {avg_pets:.2f} pets")

# What is the most common type of pet for web development students?
pets = {}
for student in students:
    if student["pets"] != [] and student["course"] == "web development":
        for pet in student["pets"]:
            if pet["species"] not in pets:
                pets[pet["species"]] = 1
            else:
                pets[pet["species"]] += 1
# sort high to low based on value
pets_sorted = sorted(pets.items(), key=lambda x: x[1], reverse=True)
print(f"The most common pet for web development students is: {pets_sorted[0][0]}")
for pet, count in pets.items():
    print(f"Web development students have {count} {pet}s")

# What is the average name length?
total_length = 0
for student in students:
    name_no_spaces = student["student"].replace(" ", "")
    total_length += len(name_no_spaces)
avg_length = total_length / len(students)
print(f"The average student name length (not including spaces) is: {avg_length:.2f}")

# What is the highest pet age for light coffee drinkers?
highest_age_pet = 0
for student in students:
    if student["pets"] != [] and student["coffee_preference"] == "light":
        for pet in student["pets"]:
            if pet["age"] > highest_age_pet:
                highest_age_pet = pet["age"]
print(f"The oldest pet among light coffee drinkers is: {highest_age_pet}")
