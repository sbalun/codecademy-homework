# List Comprehension

# Helper Methods
def print_output_seperator(example_number):
    print("#")
    print("Example " + str(example_number))
    print("#")


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
# Example XX
#
print_output_seperator(12)

# Problem: 

#
# Example XX
#
print_output_seperator(12)

# Problem: 

#
# Example XX
#
print_output_seperator(12)

# Problem: 