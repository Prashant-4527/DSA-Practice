# Approach:
'''
1. current_sum -->best sum ending at current index
2. max_sum -->best overall sum seen so far
'''


# Time Complexity: O(n)
# Space Complexity: O(1)

# Code:
def max_subarray(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum+arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

# Interview Explanation:
'''At each index, I decide whether to extend the current subarray or
start a new one. If the running sum becomes negative, starting fresh
yields a better future sum. I track the maximum encountered during traversal.
'''
