# Problem: Check if array is strictly increasing

# Approach:
1.Compare each element with previous element
2.if every element is greater than previous element
3.array is strictly increasing 

# Code:
def is_increasing(arr):
  if not arr or len(arr)<2:
    return True 

for x in range(1, len(arr)):
  if arr[x] <= arr[x-1]:
    return False

return True


# Interview Explaination:
'''To check increasing, each elements msut be greater than its previous element. I traverse from index 1 ro end to compare
with previous value. if i find any element less than or equal to previous, i return false,
if loop finishes, array is strictly increasing'''

