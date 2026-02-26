# Problem: Check is array is sorted

# Appproach:
1. Traverse array from index 0 to n-2
2. compare current element with next 
3. if current > next --> return False
4. if loop finishes --> return True

# Code:
def is_sorted(arr):
  for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
      return False
  return True

# Interview Explaination:
'''I compare each element with its next neighbour. if any pair violates non-decreasing order, I 
return Flase immediately. Otherwise the array is sorted. Worst-case time is linear, but best
case is constant due to early termination. Space is constant.'''

''' I Compare each element the next. Since no pair is violates the condition arr[i] > arr[i+1],
the array Prain non-decreasing order. Therefore the array is sorted'''

