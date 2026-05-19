# Problem: Rotate by k

# Brute Force Approach:
def rotate_by_k_brute(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    
    k = k % n  # handle k > n (k=8 on n=7 = same as k=1)

    for _ in range(k):
        last = arr[-1]
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = last

    return arr

print(rotate_by_k_brute([1, 2, 3, 4, 5, 6, 7], 3))

# Time: O(n * k), Space: O(1)



# Optimal Approach:

# Algorithm:
'''
Step 1: Handle edge cases 
        k = k % n (if k equals n, rotation brings us back to start)
        if k == 0, return as-is 

Step 2: Reverse the ENTIRE array
        arr = reverse(arr, 0, n-1)
    
Step 3: Reverse only the FIRST k elements
        arr = reverse(arr, 0, k-1)

Step 4: Reverse the REMAINING elements (from index k to end)
        arr = reverse(arr, k, n-1)

'''

def reverse(arr, left, right):
    """Helper: reverse arr in-place from index left to right"""
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-1

def rotate_k(arr, k):
    n = len(arr)

    if n == 0 or k == 0:
        return arr
    
    k = k % n   # KEY: k=7 on array of 7 = no reason  
                # k=8 on array of 7 = same as k=1

    if k == 0:  # After mod, if k is 0, already rotated
        return arr
    
    # Step 1: Reverse Entire array
    reverse(arr, 0, n-1)

    # Step 2: Reverse first k elements
    reverse(arr, 0, k-1)

    # Step 3: Reverse remaining elements
    reverse(arr, k, n-1)


    return arr


# Tests: 
print(rotate_k([1, 2, 3, 4, 5, 6, 7, 8, 8], 3))
