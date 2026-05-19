# Problem: Check if array is palindrome


# Brute Force:
def is_palindrome_brute(arr):
    return arr == arr[::-1]  # comparison with reversed copy

# Time: O(n) , Space: O(n) create a new array of same size

# Algorithm:
'''
Step 1: Set left = 0 (start), right = last index (end)
Step 2: While left < right:
            step 2a: check if arr[left] == arr[right]
            if not euqal return False 
            step 2b: move left forward
                    move right inward
step 3: if loop finishes without returning False -> return True
'''

# Optimal Solution:
def is_palindrome(arr):
    if not arr:
        return True    # Empty array -> considered palindrome
    
    left , right = 0, len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return False    # Mistmatch found -> not palindrome
        left+=1
        right-=1

    return True # All pairs matched -> palindrome

arr1 = [1, 2, 4, 2, 1]
arr2 = [1, 2, 3, 4, 5]

print(is_palindrome_brute(arr1))
print(is_palindrome_brute(arr2))
print(is_palindrome(arr1))
print(is_palindrome(arr2))
