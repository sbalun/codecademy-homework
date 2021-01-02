# Python Dictionaries 
# Scott Balun
# January 2, 2021


# Learning how to:
#
#  - Use a key to get a value from a dictionary
#  - Check for existence of keys
#  - Find the length of a dictionary
#  - Remove a key: value pair from a dictionary
#  - Iterate through keys and values in dictionaries

# # # # # Output Formatting Methods
def output_seperator():
    print("-----------------------------------------------------------")
# # # # #

# -------------------------------
#           Get a Key
# -------------------------------
# Once you have a dictionary, you can access the values in it by providing the key. 

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

# Print out the list of zodiac signs associated with the "earth" element.
print(zodiac_elements["earth"])

# Print out the list of the "fire" signs.
print(zodiac_elements["fire"])

output_seperator()
# -------------------------------
#      Get an Invalid Key
# -------------------------------
# If key does not exist will get a KeyError
# One way to avoid this error is to first check if the key exists in the dictionary:

#   key_to_check = "some string"
# 
#   if key_to_check in my_dictionary:
#     print(building_heights["some string"])

# Run the code. It should throw a KeyError! "energy" does not exist as one of the elements.
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

zodiac_elements["energy"] = "Not a Zodiac element"

# -------------------------------
#     Try/Except to Get a Key
# -------------------------------
# We saw that we can avoid KeyErrors by checking if a key is in a dictionary first. Another method we could use is a try/except:

#   key_to_check = "some string"
#   try:
#     print(building_heights["some string"])
#   except KeyError:
#     print("That key doesn't exist!")

# When we try to access a key that doesn’t exist, the program will go into the except block and print "That key doesn't exist!".

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

# Add "matcha" to the dictionary with a value of 30
caffeine_level = {"matcha": 30}

# Use a try block to try to print the caffeine level of "matcha". If there is a KeyError, print "Unknown Caffeine Level".
try:
 print(caffeine_level["matcha"])
except KeyError:
  print("Unknown Caffeine Level")

output_seperator()
# -------------------------------
#       Safely Get a Key
# -------------------------------
# Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. 
# If the key you are trying to .get() does not exist, it will return None by default

#   building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
 
#   #this line will return 632:
#   building_heights.get("Shanghai Tower")
 
#   #this line will return None:
#   building_heights.get("My House")
# -------------------------------
#
# You can also specify a value to return if the key doesn’t exist. 
# For example, we might want to return a building height of 0 if our desired building is not in the dictionary:

#   >>> building_heights.get('Shanghai Tower', 0)
#   632
#   >>> building_heights.get('Mt Olympus', 0)
#   0
#   >>> building_heights.get('Kilimanjaro', 'No Value')
#   'No Value'

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

# Use .get() to get the value of "teraCoder"‘s user ID, with 100000 as a default value if the user doesn’t exist. 
# Store it in a variable called tc_id. 
# Print tc_id to the console.
tc_id = user_ids.get('teraCoder', 100000)
print(tc_id)

# Use .get() to get the value of "superStackSmash"‘s user ID, with 100000 as a default value if the user doesn’t exist. 
# Store it in a variable called stack_id. 
# Print stack_id to the console
stack_id = user_ids.get("superStackSmash",100000)
print(stack_id)

output_seperator()
# -------------------------------
#         Delete a Key
# -------------------------------
# Sometimes we want to get a key and remove it from the dictionary.
# We can use .pop() to do this. Just like with .get(), we can provide a default value to return if the key does not exist in the dictionary
# .pop() works to delete items from a dictionary, when you know the key value

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

# In one line, add the corresponding value of the key "stamina grains" to the health_points variable and remove the item "stamina grains" from the dictionary. If the key does not exist, add 0 to health_points.
health_points += available_items.pop("stamina grains", 0)

# In one line, add the value of "power stew" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to health_points.
health_points += available_items.pop("power stew", 0)

# In one line, add the value of "mystic bread" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to health_points.
health_points += available_items.pop("mystic bread", 0)

# Print available_items and health_points
print(available_items)
print(health_points)

output_seperator()
# -------------------------------
# Get All Keys
# -------------------------------
# Sometimes we want to operate on all of the keys in a dictionary.

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# Create a variable called users and assign it to be a dict_keys object of all of the keys of the user_ids dictionary.
users = user_ids.keys()

# Create a variable called lessons and assign it to be a dict_keys object of all of the keys of the num_exercises dictionary.
lessons = num_exercises.keys()

# Print users to the console.
print(users)

# Print lessons to the console.
print(lessons)

output_seperator()
# -------------------------------
#        Get All Values
# -------------------------------
# Dictionaries have a .values() method that returns a dict_values object (just like a dict_keys object but for values!) with all of the values in the dictionary.
# There is no built-in function to get all of the values as a list, but if you really want to, you can use:
#    list(my_dict.values())

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# Create a variable called total_exercises and set it equal to 0.
total_exercises = 0

# Iterate through the values in the num_exercises list and add each value to the total_exercises variable.
for exercise in num_exercises.values():
    total_exercises += exercise

print(total_exercises)

output_seperator()
# -------------------------------
#         Get All Items
# -------------------------------
# You can get both the keys and the values with the .items() method. Like .keys() and .values(), it returns a dict_list object. 
# Each element of the dict_list returned by .items() is a tuple consisting of: (key, value)
#
# so to iterate through, you can use this syntax:

biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
 
for company, value in biggest_brands.items():
    print(company + " has a value of " + str(value) + " billion dollars. ")

# -------------------------------
output_seperator()
# -------------------------------

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

# Use a for loop to iterate through the items of pct_women_in_occupation. For each key : value pair, print out a string that looks like:
#   Women make up [value] percent of [key]s.

for key,value in pct_women_in_occupation.items():
    print("Women make up " + str(value) + " percent of " + str(key) + "s.")

output_seperator()
# -------------------------------
# Get All Keys
# -------------------------------
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# Create a variable called users and assign it to be a dict_keys object of all of the keys of the user_ids dictionary.
users = user_ids.keys()

# Create a variable called lessons and assign it to be a dict_keys object of all of the keys of the num_exercises dictionary.
lessons = num_exercises.keys()

print(users)
print(lessons)

output_seperator()
# -------------------------------
# Review
# -------------------------------

tarot = { \
    1:"The Magician", 2:"The High Priestess", 3:"The Empress", 4:"The Emperor", 5:"The Hierophant", 
    6:"The Lovers", 7:"The Chariot", 8:"Strength", 9:"The Hermit", 10:"Wheel of Fortune", 11:"Justice", 
    12:"The Hanged Man", 13:"Death", 14:"Temperance", 15:"The Devil", 16:"The Tower", 17:"The Star", 
    18:"The Moon", 19:"The Sun", 20:"Judgement", 21:"The World", 22: "The Fool"}

# reate an empty dictionary called spread.

spread = {}

# The first card you draw is card 13. Pop the value assigned to the key 13 out of the tarot dictionary and assign it as the value of the "past" key of spread.
spread["past"] = tarot.pop(13)

# The second card you draw is card 22. Pop the value assigned to the key 22 out of the tarot dictionary and assign it as the value of the "present" key of spread.
spread["present"] = tarot.pop(22)

# The third card you draw is card 10. Pop the value assigned to the key 10 out of the tarot dictionary and assign it as the value of the "future" key of spread.
spread["future"] = tarot.pop(10)

# Iterate through the items in the spread dictionary and for each key: value pair, print out a string that says: "Your {key} is the {value} card."
for key, value in spread.items():
    print("Your " + str(key) + " is the " + str(value) + " card.")

