# EXERCISE 1
# # Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.
students = ['Shamique', 'Tim', 'Josh']
print(students[1])
print(students[-1])

# EXERCISE 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "food goes here is a good food".
foods = ('spaghetti', 'salad', 'chili')
for food in foods:
    print(f"{food} is so amazing")

# EXERCISE 3
# Using a for loop, print just the last two food strings from foods.
for food in foods[-2:]:
  print(food)

# EXERCISE 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"
home_town = {
    "city": "Washington, DC", 
    "state": "USA", 
    "population": 5000000
}
print(f"I was born in {home_town['city']}, {home_town['state']} and theres a population of {home_town['population']}")

# EXERCISE 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"
for key, val in home_town.items():
  print( f"{key} = {val}" )

# EXERCISE 6
# Create an empty list named cohort
# Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:
# Iterate over cohort printing out each element 
cohort = []
for index, student in enumerate(students):
  cohort.append({
    'student': student,
    'fav_food': foods[index]
  })
for student in cohort:
  print(student)

# EXERCISE 7
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.
awesome_students = [f"{name} is so incredibly passionate about software engineering!" for name in students]
for student in awesome_students:
  print(student)


# EXERCISE 8 
# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.
a_in_foods = [food for food in foods if 'a' in food]
print(a_in_foods)