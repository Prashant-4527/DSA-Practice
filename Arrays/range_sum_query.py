# Approach;
'''
1.build prefix array once
2.answer each query using subtraction
'''

# Time Complexity: O(n + Q)
# Space Complexity: O(n)

# Code:

# Step 1 -- Preprocessing
def build_prefix(arr):
    prefix =  [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

    return prefix

# Step 2 -- Answer Queries
def range_sum(prefix, L, R):
    if L == 0:
        return prefix[R]
    return prefix[R] - prefix[L-1]

# Step 3 -- Example Usage
arr = [2, 4, 6, 8, 10]

prefix = build_prefix(arr)

print(range_sum(prefix, 1, 3))
print(range_sum(prefix, 0, 2))
print(range_sum(prefix, 2, 4))

# Interview Explaination:
'''To efficiently answer multiple range run queries, I preprocess the array
into a prefix sum array. Each Query can then be answered in constant
time using subtraction, reducing overall complexity from O(n x Q) to 
O(n + Q).
'''
