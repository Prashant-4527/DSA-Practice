# Problem: Reverse Array in Place  (Two Pointer)

# Brute Force Approach:
def reverse_brute(arr):
    n = len(arr)
    result = []

    for i in range(n-1, -1, -1):
        result.append(arr[i])

    return result 

# or simply:
def reverse_brute_v2(arr):
    return arr[::-1]   # python slicing - create new array

arr = [1, 2, 3, 4, 5]

print(reverse_brute(arr))   # [5, 4, 3, 2, 1]
#TIME : O(n)
#SPACE: O(n)



# Optimal approach (Two pointer):

def reverse_inplace(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # swap arr[left] and arr[right]
        arr[left], arr[right] = arr[right], arr[left]
        left+=1  # Move left pointer right
        right-=1 # Move right pointer left

    return arr

arr = [1, 2, 3, 4, 5]
print(reverse_inplace(arr))   # [5, 4, 3, 2, 1]

# Even Length:
arr2 = [1, 2, 3, 4] 
print(reverse_inplace(arr2))  # [4, 3, 2, 1]

# Single Element:
arr3 = [25]
print(reverse_inplace(arr3))  # [42]

# Empty:
print(reverse_inplace([]))    # []
# Time: O(n) , Space: O(1)


# Recursive Version:
def reverse_recursive(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    # Base case: pointers have met or crossed
    if left >= right:
        return arr

    # swap 
    arr[left] , arr[right] = arr[right], arr[left]


    # Recurse on the inner subarray
    return reverse_recursive(arr, left + 1, right - 1) 


arr = [1, 2, 3, 4, 5]
print(reverse_recursive(arr))
# Time : O(n), Space: O(n)

# Partial reverse:
def reverse_partical(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l+=1
        r-=1
    return arr
arr = [1, 2, 3, 4, 5]
print(reverse_partical(arr, 1, 4))
# Only reversed between index 1 and 4


# Interview Explaintion:
'''
I'll use two pointers - left starting at index 0 and right at the last index. In each iteration i swap the elements at both
pointers, then move left forward and right backward. I stop when they meet. This is O(n) time, O(1) space,- Truely in place with
no extra memory. for the recursive version the logic is identical but uses the call stack, making it O(n) space- so iterative
is preferred.
'''

