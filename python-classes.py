# Codecademy - DataScience - Python Classes
# Scott Balun
# January 12, 2021
#
# Create a Rules class so that we can explain the rules.
# Give Rules a method washing_brushes that returns the string, 
# "Point bristles towards the basin while washing your brushes."

class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

# Methods can take more arguments than self

class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile
 
converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print("5 kilometers in miles is: {} miles".format(kms_in_5_miles))
# prints "8.045"

# Above we defined a DistanceConverter class, instantiated it, and used 
# it to convert 5 miles into kilometers. Notice again that even though 
# how_many_kms takes two arguments in its definition, we only pass miles, 
# because self is implicitly passed (and refers to the object converter).

# Create a Circle class with class variable pi. Set pi to the approximation 3.14.
# Give Circle an area method that takes two parameters: self and radius. Return the 
# area as given by this formula: area = pi * radius ** 2

class Circle():
    pi = 3.14

    def area(self, radius):
        area = self.pi * radius ** 2
        return area

# Create an instance of Circle. Save it into the variable circle.
circle = Circle()

# Note: The radius of a circle is half it's diameter
# Given:
#   - A medium pizza that is 12 inches across.
#   - Your teaching table which is 36 inches across.
#   - The Round Room auditorium, which is 11,460 inches across.
#
# Calculate each of the above given circle’s area
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)








