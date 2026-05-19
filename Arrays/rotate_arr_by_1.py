# Problem: Rotate a array by 1 left:

# Approach:
1. save the first element
2. shift all the elements left 
3. first element = index n - 1

# Code:

def rotate_left_by_one(arr):
  n = len(arr)

if n == 0:
  return arr

first = arr[0]

for x in range(n-1):
  arr[x] = arr[x+1]

arr[n-1] = first

return arr


# Interview Explaination:
'''For Left rotation, i store the first element, shift remaing, elements one position left, and place store 
at the end of maintain circular order'''

