# ----------------------------------------------
# Codecademy - DataScience - Python Classes
# Student: Scott Balun
# Date: January 12, 2021
# ----------------------------------------------
#
# Note to Self:  Don't get discouraged.  Object-oriented programming is a complicated concept.
# Practice every day.  Stay with the system.  Beleive in yourself.
#
# -----------------
#   Helper Methods
# -----------------
def print_output_seperator(example_number = 2112):
    print("-------------------------------")
    print("      Example {} Output".format(str(example_number)))
    print("-------------------------------")

# -----------
#  Example 1
# -----------
print_output_seperator(1)
#
# Create a Rules class so that we can explain the rules. Give Rules a method, washing_brushes, 
# that returns the string, "Point bristles towards the basin while washing your brushes."

class Rules:

  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

# Methods can take more arguments than just self

class DistanceConverter:
    
    kms_in_a_mile = 1.609
    
    def how_many_kms(self, miles):
        return miles * self.kms_in_a_mile

    def how_many_miles(self, kilometers):
        return round(kilometers/self.kms_in_a_mile,2)
 
converter = DistanceConverter()

kms_in_5_miles = converter.how_many_kms(5)

print("5 kilometers in miles is: {} miles".format(kms_in_5_miles))
# prints "8.045"

# Above we defined a DistanceConverter class, instantiated it, and used 
# it to convert 5 miles into kilometers. 
# 
# Notice again that even though, how_many_kms, takes two arguments in its definition, we only pass miles, 
# because self is implicitly passed (and refers to the object converter).
#
# Now create a class, Circle_v1, with a class variable, pi. Set pi to the approximation 3.14.
# Give Circle_v1 an area method that takes two parameters: self and radius. 
# Return the area as given by this formula: area = pi * radius ** 2

class Circle_v1():
    
    pi = 3.14

    def area(self, radius):
        return self.pi * radius ** 2

# Create an instance of Circle_v1. Save it into the variable circle.
circle = Circle_v1()

# Note: The radius of a circle is half it's diameter
# Given that:
#
#   - A medium pizza that is 12 inches across.
#   - Your teaching table which is 36 inches across.
#   - The Round Room auditorium, which is 11,460 inches across.
#
# Calculate the area for each of the above

pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

# -----------
#  Example 2
# -----------
print_output_seperator(2)
#
# -------------------------------------------------
# Magic or Dunder Methods...i.e., Constructors
# -------------------------------------------------
# Dunder methods, so-named because they have two underscores 
# (double-underscore abbreviated to “dunder”) on either side of them.
#
# The first dunder method we’re going to use is the __init__() method 
#   - Note the two underscores before and after the word “init” 
#   - This method is used to initialize a newly created object. 
#   - It is called every time the class is instantiated.
#
# Methods that are used to prepare an object being instantiated are called constructors. 
# The word “constructor” is used to describe similar features in other OOP languages but 
# programmers who refer to a constructor in Python are usually talking about the __init__() method.

class Shouter_v1:

  def __init__(self):
    print("HELLO?!")
 
shout1 = Shouter_v1()
# prints "HELLO?!"
 
shout2 = Shouter_v1()
# prints "HELLO?!"

# Note the above class called Shouter_v1
# Every time we create an instance of Shouter the program prints out a shout. 
# Pay careful attention to the instantiation syntax used. 
# We could pass parameters to it and those parameters will be received by the __init__() method.

class Shouter:

  def __init__(self, phrase):
      if type(phrase) == str:
          print(phrase.upper())
 
shout1 = Shouter("shout")
# prints "SHOUT"
 
shout2 = Shouter("shout")
# prints "SHOUT"
 
shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"

# Above the updated Shouter class can now take the additional parameter, phrase. 
# When we created each of our objects we passed an argument to the constructor. 
# The constructor takes the argument, phrase, and if it’s a string, prints out 
# the all-caps version of phrase.
# -----------
#  Example 3
# -----------
print_output_seperator(3)
#
# Add a constructor to our Circle class.
# It should take the argument diameter.
#
# Have the constructor print out the message "New circle with diameter: {diameter}" 
# when a new circle is created.

class Circle_v2:
    pi = 3.14
    
    def __init__(self, diameter):
        print("New circle with diameter: {}".format(diameter))

    def area(self, radius):
        area = self.pi * radius ** 2
        return area

# Create a circle, teaching_table, with diameter 36.
teaching_table = Circle_v2(36)


# -------------------------------------------------
#                Instance Variables
# -------------------------------------------------

class Store:
    pass

# Create two objects from the above store class
# Name them alternative_rocks and isabelles_ices
alternative_rocks = Store()
isabelles_ices = Store()

# Give them both instance attributes called store_name. Set alternative_rocks‘s 
# store_name to "Alternative Rocks". Set isabelles_ices‘s store_name to "Isabelle's Ices".
alternative_rocks.store_name ="Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"
# -----------
#  Example 4
# -----------
print_output_seperator(4)
#
# -------------------------------------------------
#                Attribute Functions
# -------------------------------------------------
#
# Below is a list of different data types: a dictionary, a string, an integer, and a list 
# All saved in the variable can_we_count_it.

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

# For every element in the list, check if the element has the attribute count using the 
# hasattr() function. If so, print the following line of code:#
#
#   print(str(type(element)) + " has the count attribute!")
#
# Add an else statement for the elements that do not have the attribute count. 
# In this else statement add the following line of code: 
#
#   print(str(type(element)) + " does not have the count attribute :(")

for element in can_we_count_it:
    if hasattr(element, "count"):
        print(str(type(element)) + " has the count attribute!")
    else:
        print(str(type(element)) + " does not have the count attribute :(")
# -----------
#  Example 5
# -----------
print_output_seperator(5)
#
# -------------------------------------------------
#                      Self
# -------------------------------------------------
#
# Here is our familiar friend, the Circle class.  Even though we usually 
# know the diameter beforehand what we need for most calculations is the radius.
# 
#   - In Circle‘s constructor, __init__(), set the instance variable, self.radius,
#     to equal half the diameter that gets passed in.
#
#   - Define a method, circumference, that takes only one argument, self, and returns 
#     the circumference of a circle with the given radius by this formula:  circumference = 2 * pi * radius

class Circle_v3:

    pi = 3.14
    
    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        self.radius = diameter/2

    def circumference(self):
        return 2 * self.pi * self.radius

# Define three Circles with three different diameters.
#   - A medium pizza that is 12 inches across.
#   - Your teaching table which is 36 inches across.
#   - The Round Room auditorium which is 11,460 inches across.

medium_pizza = Circle_v3(12)
teaching_table = Circle_v3(36)
round_room = Circle_v3(11460)

# -----------
#  Example 6
# -----------
print_output_seperator(6)
#
# Print out the circumferences of medium_pizza, teaching_table, and round_room.
print("The circumference of the medium pizza is: {x}".format(x=medium_pizza.circumference()))
print("The circumference of the teaching table is: {x}".format(x=teaching_table.circumference()))
print("The circumference of the round room is: {x}".format(x=round_room.circumference()))

# -------------------------------------------------
#            Everything is an Object
# -------------------------------------------------
#
# -----------
#  Example 7
# -----------
print_output_seperator(7)
#
# Call dir() on the number 5. Print out the results.
print(dir(5))

# -----------
#  Example 8
# -----------
print_output_seperator(8)
#
# Define a function called this_function_is_an_object. It can take any parameters and return anything you’d like.
def this_function_is_an_object(x, y):
    return x, y

# Print out the result of calling dir() on this_function_is_an_object.
# Functions are objects too!
print("This is the output from calling dir() on the function this_function_is_an_object:\n {x}".format(x=dir(this_function_is_an_object)))

# -------------------------------------------------
#                String Representation
# -------------------------------------------------
#
# We previously learned about the dunder method __init__(). 
# Now, we will learn another dunder method called __repr__(). 
# 
# The __repr__() is a method we can use to tell Python what we want 
# the string representation of the class to be.
#
#  __repr__() can only have one parameter, self, and must return a string.
#
# Add a __repr__() method to the Circle class that returns Circle with radius {radius}

class Circle:
    pi = 3.14
    
    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        self.radius = diameter / 2

    def __repr__(self):
        return print("Circle with radius {}".format(str(self.radius)))

    def circumference(self):
        return 2 * self.pi * self.radius

# -----------
#  Example 9
# -----------
print_output_seperator(9)
#
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

# ------------------------
#  Review Exercises
# ------------------------
print_output_seperator(10)
# 
# Define a class Student
# Add a constructor for Student. 
#   - Have the constructor take in two parameters: a name and a year. 
#   - Save those two as attributes .name and .year
#
# In the body of the constructor for Student, declare self.grades, as an empty list
# Add an .add_grade() method that takes a parameter, grade
#   - .add_grade() should verify that grade is of type, Grade, and if so, add it to the Student‘s .grades.
#   - If grade isn’t an instance of Grade then .add_grade() should do nothing.

class Student:
    
    attendance = {}
    
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)

    def get_average(self):
        sum_of_grades = 0
        for grade in self.grades:
            sum_of_grades += grade

        return sum_of_grades / len(self.grades)

# Create three instances of the Student class:
#
#   - Roger van der Weyden, year 10
#   - Sandro Botticelli, year 12
#   - Pieter Bruegel the Elder, year 8
#
# Save them into the variables roger, sandro, and pieter.  
# 
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder",8)

# Create a class, Grade, with minimum_passing as an attribute set to 65
# Give Grade a constructor. 
#   - Take in a parameter score and assign it to self.score

class Grade:
    #
    # grade = Grade(nn)
    #
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    def __repr__(self):
        return f'Grade.grade({self.score})'

    def is_passing(self):
        if self.score < self.minimum_passing:
            return 'Failed'

        return 'Passed'

pieter.add_grade(Grade(100))
pieter.add_grade(Grade(90))
pieter.add_grade(Grade(77))
print(pieter.grades)

# Write a Grade method .is_passing() that returns whether a Grade has a passing .score.
# Write a Student method get_average() that returns the student’s average score.
# Add an instance variable to Student that is a dictionary called .attendance, 
# With dates as keys and booleans as values that indicate whether the student attended school that day.
