# Problem: Find Maximum Element in Array

# Approach:
# 1. Assume first element is maximum
# 2. Traverse remaining elements
# 3. If current element is greater → update max
# 4. Return max value

# Time Complexity: O(n)
# Space Complexity: O(1)

# Interview Explanation:
# I scan the array once while tracking the largest value seen so far.
# Whenever I find a larger element, I update the maximum.
# This requires linear time and constant space.


# Code:
def find_max(arr):
    if not arr:
        return None
    
    max_val = arr[0]

    for x in arr[1:]:
        if x > max_val:
            max_val = x
    return max_val

#Example:
Input: [4, 2, 5, 3]
Output: 5
