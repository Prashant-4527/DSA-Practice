Problem: Find Minimum Element in Array

# Approach:
1. Assume first element is minimum
2. traverse remaining elements 
3. if current < min --- update
4. return min

Time Complexity: O(n)
Space Complexity: O(1)

# Interview explaination:
'''I maintain the smallest value seen so far while scanning the array once.
each element is compared once, giving theta(n) time.
Only constant auxiliary memeory is used, so space is O(1)'''

Code:
def find_min(arr):
    if not arr:
        return None
    min_val = arr[0]

    for x in arr[1:]:
        if x < min_val:
            min_val = x

    return min_val
