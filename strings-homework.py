# Python Loops Homework
# Scott Balun
# December 28, 2020
#
# In this lesson I will learn about the following string methods:

# - .upper(), .title(), and .lower() adjust the casing of your string.
# - .split() takes a string and creates a list of substrings.
# - .join() takes a list of strings and creates a string.
# - .strip() cleans off whitespace, or other noise from the beginning and end of a string.
# - .replace() replaces all instances of a character/string in a string with another character/string.
# - .find() searches a string for a character/string and returns the index value that character/string is found at.
# - .format() allows you to interpolate a string with variables.

####   Helper Methods   ####
def print_output_seperator(example_number = 99999):
    print("# ----------------")
    print("# Problem " + str(example_number) + " Output")
    print("# ----------------")
####    ####    ####    ####

print_output_seperator(1)
# ------------
# Problem 1 - Splitting Strings II
# ------------
# 
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

#  Problem: Using .split() and the provided string, create a list called author_names containing each individual author name as it’s own string.
authors_names = authors.split(",")

# Create another list called author_last_names that only contains the last names of the poets in the provided string.
author_last_names = []

for name in authors_names:
    seperate_fname_and_lname = name.split(" ")
    l_name_only = seperate_fname_and_lname[-1]
    author_last_names.append(l_name_only)

# Test the contents of the new last name only list
print(author_last_names)
#
print_output_seperator(2)
# ------------
# Problem 2 - Splitting Strings III
# ------------
# 
# We can also split strings using escape sequences. Escape sequences are used to indicate that we want to split
# by something in a string that is not necessarily a character. The two escape sequences we will cover here are
#
#  \n Newline
#  \t Horizontal Tab
#
# Problem: Create a list called spring_storm_lines that contains a string for each line of Spring Storm.

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)
#
print_output_seperator(3)
# ------------
# Problem 3 - Joining Strings
# ------------
# 
# .join() is essentially the opposite of .split(), it joins a list of strings together with a given delimiter.
#
# Problem: Use .join() to combine these words into a sentence and save that sentence as the string reapers_line_one.
#
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = " ".join(reapers_line_one_words)

# Test contents of new list, reapers_line_one
print(reapers_line_one)
#
print_output_seperator(4)
# ------------
# Problem 4 - Joining Strings II
# ------------
# You can use any type of delimter with .join.  Not just space.  Could be comma or other delimter like tab or new-line \n
#
# Problem Statement:  Join the strings in the list. winter_trees_lines, together into a single string that can be used to display the full poem. Name this string winter_trees_full.
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)

# Test contents of winter_trees_full list
print(winter_trees_full)
#
print_output_seperator(5)
# ------------
# Problem 5 - .strip()
# ------------
#
# Problem Statement: Use .strip() on each line in the follwing list to remove the unnecessary whitespace and save it as a new list, love_maybe_lines_stripped.

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []

for line in love_maybe_lines:
    love_maybe_lines_stripped.append(line.strip())

# Test contents of love_maybe_lines_stripped list 
print(love_maybe_lines_stripped)
print('\n')

# Problem Statemeant: .join() the lines in, love_maybe_lines_stripped, together into 
# one large multi-line string, love_maybe_full, that can be printed to display the poem.
# Each line of the poem should show up on its own line.
love_maybe_full = '\n'.join(love_maybe_lines_stripped)

# Test contents of love_maybe_fulld string 
print(love_maybe_full)
#
print_output_seperator(6)
#
# ------------
# Problem 6 - .Replace()
# ------------
# Problem Statement: Use .replace() to change all instances of 'Tomer' to 'Toomer' in the, toomer_bio, string shown below. 
# Save the updated bio to the string, toomer_bio_fixed

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")

# Test contents of string 
print(toomer_bio_fixed)
#
print_output_seperator(7)
#
# ------------
# Problem 7 - .find()
# ------------
# Problem Statement: At what index place does the word “disown” appear? Save that index place to the variable disown_placement

god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find('disown')

# Test contents of variable
print(disown_placement)
#
print_output_seperator(8)
# ------------
# Problem 8 - .format()
# ------------
# Problem Statement: Write a function called poem_title_card that takes two inputs: 
# the first input should be, title, and the second, poet. 
# The function should use .format() to return the following string: "The poem "[TITLE]" is written by [POET]."

def poem_title_card(title, poet):
   return "The poem \"{}\" is written by {}.".format(title,poet)

# Test the return output of the poem_title_card function
print(poem_title_card("The Mighty Van Halen","Steve Rosen"))

#
print_output_seperator(9)
# ------------
# Problem 9 - .format() II
# ------------
# Problem Statement: The function, poem_description, is supposed to use .format() to print out some quick information about a poem, but it seems to be causing some errors currently.
# Fix the function by using keywords in the .format() method.

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

# Run poem_description with the following arguments and save the results to the variable my_beard_description:
# - author = "Shel Silverstein"
# - title = "My Beard"
# - original_work = "Where the Sidewalk Ends"
# - publishing_date = "1974"

my_beard_description = poem_description(1974, "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")

print(my_beard_description)
#
print_output_seperator(10)
# ------------
# Problem 10 - Review
# ------------
# Problem Statement: Start by splitting, highlighted_poems, list below at the commas and saving it to, highlighted_poems_list.
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print("\nPrinting the string: highlighted_poems")
print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')
print("\nPrinting the list: highlighted_poems_list")
print(highlighted_poems_list)

# Create a new empty list, highlighted_poems_stripped.
# Iterate through highlighted_poems_list using a for loop and for each poem strip away the whitespace and append it to your new list, highlighted_poems_stripped
highlighted_poems_stripped = []

for poem in highlighted_poems_list:
    highlighted_poems_stripped.append(poem.strip())

print("\nPrinting the list: highlighted_poems_stripped")
print(highlighted_poems_stripped)

# break up all the information for each poem into it’s own list, so we end up with a list of lists.
# Create a new empty list called, highlighted_poems_details.

highlighted_poems_details = []

for poem in highlighted_poems_stripped:
    highlighted_poems_details.append(poem.split(':'))

print("\nPrinting the list: highlighted_poems_details")
print(highlighted_poems_details)
print('\n')

# Create three new empty lists: titles, poets, dates
titles = []
poets = []
dates = []

# Separate out all of the titles, the poets, and the publication dates into their own lists.
for i in range(len(highlighted_poems_details)):
    title, poet, date  = highlighted_poems_details[i]
    titles.append(title)
    poets.append(poet)
    dates.append(date)

print("\nPrinting the TITLES only list:")
print(titles)
print("\nPrinting the POETS only list:")
print(poets)
print("\nPrinting the DATES only list:")
print(dates)
print("\n")

# Write a for loop that uses .format() to print out the following string for each poem:
# The poem TITLE was published by POET in DATE.

for i in range(len(highlighted_poems_details)):
    poem, poet, date  = highlighted_poems_details[i]
    print("The poem {} was published by {} in {}".format(poem,poet,date))