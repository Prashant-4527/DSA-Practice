# Problem: Count Frequency of Each Element

# Brute Force Approach: 
def count_freq_brute(arr):
    n = len(arr)
    counted = set()  # skip the already counted elements
    result = {}

    for i in range(n):
        if arr[i] in counted: 
            continue   # already counted skip karo

        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count+=1

        result[arr[i]] = count
        count.add(arr[i])

    return result

# Time: O(n^2), Space: O(n)



# Optimal Approach:

# Algorithm:
'''
Step 1: Make a Empty Dict - freq {}
Step 2: For each element in array:
    Step 2a: Check - if this element already appread
    Step 2b: if yes -> count+=1
             if no -> count = 1
Step 3: Return dict

'''

def count_freq(arr):
    if not arr:
        return {}
    
    freq = {}


    for num in arr:
        freq[num] = freq.get(num, 0) + 1 


    return freq


arr = [1, 2, 3, 4, 5, 5, 5, 4, 6, 44, 55, 1]

print(count_freq(arr))

