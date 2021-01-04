# codecademy code-challenge string methods
# Scott Balun
# January 2, 2020
#
# -------- Output Formatting Methods -------- 
def output_seperator():
    print("-----------------------------------------------------------")
#  
output_seperator()
# -------------------
#    Count Letters
# -------------------
# unique_english_letters(word)

# Write a function called unique_english_letters that takes the string word as a parameter. 
# The function should return the total number of unique letters in the string. 
# Uppercase and lowercase letters should be counted as different letters.  
# We’ve given you a list of every uppercase and lower case letter in the English alphabet. 
# It will be helpful to include that list in your function.


# Write your unique_english_letters function here:
def unique_english_letters(word):

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    start_len = len(letters)
    
    for letter in word:
        if letter in letters:
            letters = letters.replace(letter,"")

    return start_len - len(letters)

# Uncomment these function calls to test your function:
print("The number of unique letters in the string mississippi is: " + str(unique_english_letters("mississippi")))
# should print 4

print("The number of unique letters in the string Apples is: " + str(unique_english_letters("Apples")))
# should print 5
# 
output_seperator()

# -------------------
#      Count X
# -------------------
# count_char_x()
# Write a function named count_char_x that takes a string named word and a single character named x as parameters. 
# The function should return the number of times x appears in word.   

def count_char_x(word, x):
    count = 0
    for letter in word:
        if letter == x:
            count += 1
    return count

# Testing count_char_x
print("The number of times 's' appears in 'mississippi': " + str(count_char_x("mississippi","s")))
# should print 4
print("The number of times 'm' appears in 'mississippi': " + str(count_char_x("mississippi","m")))
# should print 1

output_seperator()

# -------------------
#    Count Multi X
# -------------------
# count_multi_char_x()
# 
# Write a function named count_multi_char_x that takes a string named word and a string named x. 
# This function should do the same thing as the count_char_x function you just wrote - it should 
# return the number of times x appears in word. However, this time, make sure your function works 
# when x is multiple characters long.

#  For example, count_multi_char_x("Mississippi", "iss") should return 2

def count_multi_char_x(word, x):
    # Use split() to remove the 'x' phrase from our 'word'
    word_as_list = word.split(x)
    # Use .join to recombine the list items in word_as_list back into a single string
    word_with_x_removed = "".join(word_as_list)
    # Count the number of occurences of 'x' phrase in 'word'
    num_occurences_of_x_in_word = (len(word) - len(word_with_x_removed)) / len(x)
    return int(num_occurences_of_x_in_word)

# Testing function, count_multi_char_x
print("The number of times 'iss' appears in the word 'mississippi' : " + str(count_multi_char_x("mississippi","iss")))

#
output_seperator()
# -------------------
#  Substring Between
# -------------------
# substring_between_letters()
# Write a function named substring_between_letters that takes a string named word, a single character named start, 
# and another character named end. This function should return the substring between the first occurrence of start 
# and end in word. If start or end are not in word, the function should return word.
#
# For example, substring_between_letters("apple", "p", "e") should return "pl".

def substring_between_letters(word, start, end):
    if start in word and end in word:
        # Use .index() method to get the index of the first letter of the substring that begins after 'start'
        start_index = word.index(start) + 1
        # Use the .index() method to get the index of the 'end' character
        end_index =  word.index(end)
        # Use list slicing to extract the substring between the 'start' and 'end' characters.  Return that substring
        return word[start_index:end_index]

    return word

# Testing the method substring_between_letters
print("This should return 'pl' : " + substring_between_letters("apple", "p", "e"))
# should print "pl"
print("This should return 'apple' : " + substring_between_letters("apple", "p", "c"))
# should print "apple"



#
output_seperator()
# -------------------
#
# -------------------



#
output_seperator()
# -------------------
#
# -------------------