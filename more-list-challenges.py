
def every_three_nums(start):
  lst = []
  if start < 100:
    for i in range(start,103,3):
      lst.append(i)

  return lst

# Test the function
print(every_three_nums(91))

