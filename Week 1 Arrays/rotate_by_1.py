# Problem: Rotate by 1

# Algorithm (Rotate right):
'''
Step 1: if array has 0 or 1 elements -> return as-is
Step 2: Save the last element in a temp variable
Step 3: Shift element one position to the RIGHT
Step 4: Place the saved last element at index 0
Step 5: Return array

'''

# Optimal approach for rotate by 1: 
def rotate_right(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    last = arr[n-1]   # save the last element

    for i in range(n-1, 0, -1):  # Shift everything right
        arr[i] = arr[i-1]
    
    arr[0] = last   # Put saved element at front

    return arr




# Algorithm (Rotate left):
'''
Step 1: if array has 0 or 1 elements -> return as-is
Step 2: Save the first element in a temp variable
Step 3: Shift element one position to the LEFT
Step 4: Place the saved first element at last index
Step 5: Return array

'''



def rotate_left(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    first = arr[0]   # save the first element

    for i in range(0, n-1):  # Shift everything left
        arr[i] = arr[i+1]
    
    arr[n-1] = first   # Put saved element at end

    return arr

# Time: O(n), Space: O(1)


# Tests:
print(rotate_left([1, 2, 3, 4, 5]))
print(rotate_right([1, 2, 3, 4, 5]))

