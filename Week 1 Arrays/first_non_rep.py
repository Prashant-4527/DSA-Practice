# Problem: First Non-Repeating Element

# Brute Force Approach:
def first_non_repeating_brute(arr):
    n = len(arr)
    for i in range(n):
        is_unique = True
        for j in range(n):
            if i != j and arr[i] == arr[j]:
                is_unique = False
        if is_unique:
            return arr[i]
            
    return -1  

# Time: O(n^2), Space: O(1)



# Optimal Approach: 
'''
Pass 1: Freaquency count:
    Step 1: Make a empty dict
    Step 2: count every element in dict

Pass 2: Find first unique:
    Step 3: Go through in original array order
    Step 4: Check every element - if freq == 1
    Step 5: Return first element where freq == 1
    Step 6: If not found return -1
'''


# Code:
def find_first_non_repeat_element(arr):
    if not arr:
        return -1
    
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0)+1


    for num in arr:
        if freq[num] == 1:
            return num
    return -1

# Test case: 
print(find_first_non_repeat_element([1, 2, 3, 4, 5, 1, 2, 3, 4])) # 5