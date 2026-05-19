# Problem: Rotate a array right

# Approach:
1. save the last element
2. move the each value one step ahead
3. index 0 = last element

# Code:

def rotate_array(arr):
  n = len(arr)

  if n == 0:
    return arr

  for x in range(n-1, 0, -1):
    arr[x] = arr[x-1]

  arr[0] = last

  return arr


# Interview Explaination:
'''To rotate right by one, i store the last element, shift all element one step to the right, and place
the stored value at index 0.  This presevers circular order'''


