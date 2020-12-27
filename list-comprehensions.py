# List Comprehension
#
# The  exercises that follow will be practice on basic list comprehension syntax like:

temperatures = [-5, 29, 26, -7, 1, 18, 12, 31]
temperatures_adjusted = [temp + 20 for temp in temperatures]

# and basic zip syntax like:
x = zip([1, 2, 3], [4, 6, 8])

# Also, along the way  will be practicing these core Python concepts:
"""
* Strings and substrings
* Getting characters from an index
* Boolean operators and comparators
* Mathematical operations
* String concatenation
* Casting from an integer to a string
"""
####   Helper Methods   ####
def print_output_seperator(example_number = 2112):
    print("#")
    print("Example " + str(example_number))
    print("#")
#
#
#
# Example 1
#
print_output_seperator(1)

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

"""
This list comprehension:

1. Takes an element in heights
2. Assigns that element to a variable called x_height
3. Checks if x_height > 161.  If so, adds that value to can_ride_coaster
4. Repeats steps 1-3 for all of the values in heights

"""
can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)
#
# Example 2
#
print_output_seperator(2)

celsius = [0, 10, 15, 32, -5, 27, 3]

"""
This list comprehension

1. Takes and element from the list, celsius
2. Assigns this value to the variable temp
3. Multiply the value of temp by 9/5 +32 and add this calculated value to the list, fahrenheit 
"""

fahrenheit = [temp * 9/5 + 32 for temp in celsius]

print(fahrenheit)
#
# Example 3
#
print_output_seperator(3)

nums = [4, 8, 15, 16, 23, 42]

"""
The list comprehension that follows will:

1. Take an element from the list, nums
2. Assign this value to the variable, number
3. number % 2 will yeild a 0 when number is an even number, 1 when number is an odd number
4. The value of the modulo operation from step 3 will be assigned to the list, parity

"""

parity = [number % 2 for number in nums]

print(parity)

#
# Example 4
#
print_output_seperator(4)

# Problem: Create a new list named greetings that adds "Hello, " in front of each name in the list names.

names = ["Elaine", "George", "Jerry", "Cosmo"]
greetings = ["Hello, "+ name for name in names]

print(greetings)

#
# Example 5
#
print_output_seperator(5)

names = ["Elaine", "George", "Jerry", "Cosmo"]
#
# Problem: Create a new list named first_character that contains the first character from every name in the list names
#
first_character = [name[0] for name in names]
print(first_character)

#
# Example 6
#
print_output_seperator(6)

names = ["Elaine", "George", "Jerry", "Cosmo"]

# Problem: Create a new list named lengths that contains the size of each name in the list of names

lengths = [len(name) for name in names]

print(lengths)

#
# Example 7
#
print_output_seperator(7)

booleans = [True, False, True]

# Problem: Create a new list named opposite that contains the opposite boolean for each element in the list booleans.
opposite =[not bools for bools in booleans]

print(opposite)

#
# Example 8
#
print_output_seperator(8)

names = ["Elaine", "George", "Jerry", "Cosmo"]
# Problem: Create a new list called is_Jerry, in which an entry at position i is True if the 
# entry in names at position i equals "Jerry". The entry should be False otherwise

is_Jerry = [name == "Jerry" for name in names]

print(is_Jerry)

#
# Example 9
#
print_output_seperator(9)

nums = [5, -10, 40, 20, 0]

# Problem: Create a new list called greater_than_two, in which an entry at position i is True if the entry in nums at position i is greater than 2.
greater_than_two = [number > 2 for number in nums]

print(greater_than_two)

#
# Example 10
#
print_output_seperator(10)

nested_lists = [[4, 8], [15, 16], [23, 42]]
# Problem: Create a new list named product that contains the product of each sub-list of nested_lists.
product = [num1 * num2 for (num1,num2) in nested_lists]

print(product)
#
# Example 11
#
print_output_seperator(11)

nested_lists = [[4, 8], [16, 15], [23, 42]]

# Problem: Create a new list named greater_than that contains True if the first number in the 
# sub-list is greater than the second number in the sub-list, and False otherwise.

greater_than = [num1 > num2 for (num1,num2) in nested_lists]

print(greater_than)

#
# Example 12
#
print_output_seperator(12)

nested_lists = [[4, 8], [16, 15], [23, 42]]

# Problem: reate a new list named first_only that contains the first element in each sub-list of nested_lists.

first_only = [num1 for (num1,num2) in nested_lists]

print(first_only)

#
# Example 13
#
print_output_seperator(13)

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
# Problem: Use list comprehension and the zip function to create a new list 
# named sums that sums corresponding items in lists a and b. For example, 
# the first item in the new list should be 5 from adding 1 and 4 together.
sums = [num1 + num2 for (num1, num2) in list(zip(a,b))]

print(sums)
#
# Example 14
#
print_output_seperator(14)
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
# Problem: Use list comprehension and the zip function to create a new list named 
# quotients that divides the elements in list b by those in list a . For example, 
# the second item in the new list should be 2.5 from dividing 5.0 by 2.0
quotients = [num2/num1 for (num1,num2) in list(zip(a,b))]
print(quotients)
#
# Example 15
#
print_output_seperator(15)
capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]
# Problem:You’ve been given two lists: a list of capitals and a list of countries. 
# Create a new list named locations that contains the string "capital, country" for 
# each item in the original lists. For example, if the 5th item in the capitals list 
# is "Lima" and the 5th item in the countries list is "Peru", then the 5th item in the 
# new list should be "Lima, Peru"
locations = [cap + ", " + ctr for (cap,ctr) in list(zip(capitals,countries))]
print(locations)
#
# Example 16
#
print_output_seperator(16)
names = ["Shilah", "Arya", "Kele"]
ages = [14, 9, 35]
# Problem: Given two lists: a list of names and a list of ages. Create a new list named 
# users that contains the string "Name: name, Age: age" for each pair of elements in the 
# original lists. For example, if the 5th item in the names list is "Aiyana" and the 
# 5th item in ages is 42, then the 5th item in the new list should be "Name: Aiyana, Age: 42".
users = ["Name: " + name + ", Age: " +  str(age) for (name,age) in list(zip(names,ages))]
print(users)
#
# Example x
print_output_seperator(17)
#
a = [30, 42, 10]
b = [15, 16, 17]
# Problem: Create a new list named greater_than that contains True or False depending on whether 
# the corresponding item in list a is greater than the one in list b. For example, if the 2nd 
# item in list a is 3, and the 2nd item in list b is 5, the 2nd item in the new list should be False.
#
greater_than = [num_frm_a > num_frm_b for (num_frm_a,num_frm_b) in list(zip(a,b))]
print(greater_than)
# Example x
print_output_seperator()
#
# Problem:
#
# Example x
print_output_seperator()
#
# Problem:
#
