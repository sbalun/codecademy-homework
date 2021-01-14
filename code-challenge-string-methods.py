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
print("The number of unique letters in the string 'mississippi' is: " + str(unique_english_letters("mississippi")))
# should print 4

print("The number of unique letters in the string 'Apples' is: " + str(unique_english_letters("Apples")))
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
#    X Length
# -------------------
# x_length_words()
# Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. 
# This function should return True if every word in sentence has a length greater than or equal to x.

def x_length_words(sentence, x):
    all_words_greater_or_equal_to_x = True
    word_list = sentence.split()

    for word in word_list:
        if len(word) < x:
            all_words_greater_or_equal_to_x = False

    return all_words_greater_or_equal_to_x

# Testing the function, x_length_words
print("The output for 'x_length_words' should be False: " + str(x_length_words("i like apples", 2)))
# should print False
print("The output for 'x_length_words' should be True: " + str(x_length_words("he likes apples", 2)))
# should print True
#
output_seperator()
# -------------------
#    Check Name
# -------------------
# check_for_name()
# Write a function called check_for_name that takes two strings as parameters named sentence and name.
# The function should return True if name appears in sentence in all lowercase letters, all uppercase letters, 
# or with any mix of uppercase and lowercase letters. The function should return False otherwise.
#
# For example, the following three calls should all return True:
#   check_for_name("My name is Jamie", "Jamie")
#   check_for_name("My name is jamie", "Jamie")
#   check_for_name("My name is JAMIE", "Jamie")

def check_for_name(sentence, name):
    sentence_as_list = sentence.split()
    sentence_in_lower_case = []
    for word in sentence_as_list:
        sentence_in_lower_case.append(word.lower())
    new_sentence = "".join(sentence_in_lower_case)
    lower_name = name.lower()
    return lower_name in new_sentence

print("This should print True: " + str(check_for_name("My name is Jamie", "Jamie")))
# should print True
print("This should print True: " + str(check_for_name("My name is jamie", "Jamie")))
# should print True
print("This should print False: " + str(check_for_name("My name is Samantha", "Jamie")))
# should print False

output_seperator()
# -------------------
# Every Other Letter
# -------------------
# every_other_letter()
# Create a function named every_other_letter that takes a string named word as a parameter. 
# The function should return a string containing every other letter in word.

def every_other_letter(word):
    every_other_letter =[]
    for index in range(len(word)):
        if index % 2 == 0:
            every_other_letter.append(word[index])

    return "".join(every_other_letter)

print("This encrypted sentence, caoloil^ !i7t- -fprmilcpkpenn- -w8o9rnk!s?!, actually says: " + str(every_other_letter("caoloil^ !i7t- -fprmilcpkpenn- -w8o9rnk!s?!")))

output_seperator()
# -------------------
#      Reverse
# -------------------
# reverse_string()
# Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.

def reverse_string(word):
    reverse_word = []
    for index in range(len(word)-1, -1, -1):
        reverse_word.append(word[index])

    return "".join(reverse_word)

print("This should print ymedacedoC: " + reverse_string("Codecademy"))
print("This should print !dlrow olleH: " + reverse_string("Hello world!"))
print("This should print : " + reverse_string(""))

output_seperator()
# -------------------
#  Make Spoonerism     
# -------------------
# make_spoonerism()
# Write a function called make_spoonerism that takes two strings as parameters named word1 and word2. 
# Finding the first syllable of a word is a difficult task, so for our function, we’re going to switch 
# the first letters of each word. Return the two new words as a single string separated by a space.

def make_spoonerism(word1, word2):
    return word2[0] + word1[1:len(word1)] + " " + word1[0] + word2[1:len(word2)]

# Testing the function make_spoonerism
print("This should print 'Lodecademy Cearn': " + make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print("This should print 'wello Horld!': " + make_spoonerism("Hello", "world!"))
# should print wello Horld!
print("This hould print 'b a': " + make_spoonerism("a", "b"))
# should print b a

output_seperator()
# -------------------
#   Add Exclamation     
# -------------------  
# add_exclamation()
# Create a function named add_exclamation that has one parameter named word. 
# This function should add exclamation points to the end of word until word is 
# 20 characters long. If word is already at least 20 characters long, just return word.

def add_exclamation(word):
    if len(word) >= 20:
        return word
    else:
        while len(word) < 20:
            word += "!"

    return word

print("This should print 'Codecademy!!!!!!!!!!': " + add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print("This should print 'Codecademy is the best place to learn': " + add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn