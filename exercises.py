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





# EXERCISE 6