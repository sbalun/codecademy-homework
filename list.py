"""
1. Append Sum
Write a function named append_sum that has one parameter — a list named named lst.
The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.

For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].
"""

#Write your function here
def append_sum(lst):
  x=0
  while x < 3:
    lst.append( lst[-1] + lst[-2] )
    x += 1
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

"""
2. Larger lists
Write a function named larger_list that has two parameters named lst1 and lst2.

The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.
"""

#Write your function here
def larger_list(lst1,lst2):

  if len(lst1) >= len(lst2):
    last_element = lst1[-1]
  elif len(lst1) < len(lst2):
    last_element = lst2[-1]

  return last_element

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

"""
3. More Than N

Create a function named more_than_n that has three parameters named lst, item, and n.

The function should return True if item appears in the list more than n times. The function should return False otherwise.
"""

#Write your function here
def more_than_n(lst,item,n):
  count = 0
  for thing in lst:
    if thing == item:
      count += 1
  
  if count > n:
    return True
  else:
    return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

"""
4. Append Size

Create a function called append_size that has one parameter named lst.
The function should append the size of lst (inclusive) to the end of lst. The function should then return this new list.

For example, if lst was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of lst was originally 3.
"""

