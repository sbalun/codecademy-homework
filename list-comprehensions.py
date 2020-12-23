# List Comprehension

#
# Example 1
#

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
nums = [4, 8, 15, 16, 23, 42]

"""
The list comprehension that follows will:

1. Take an element from the list, nums
2. Assign this value to the variable, number
3. number % 2 will yeild a 0 when number is an even number, 1 when number is an odd number
4. The value of the modulo operation from step 3 will be assigned to the list, parity

"""

parity = [number % 2 for number in nums]

parity