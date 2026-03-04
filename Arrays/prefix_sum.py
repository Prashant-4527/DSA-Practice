# Approach:
'''
1.Create prefix array same size
2.prefix[0] = arr[0]
3.for each index i:
prefix[i] = prefix[i-1] + arr[i]
'''
# Time complexity: building prefix: O(n) or Range Query: O(1)
# Space complexity: O(n)

# Code for build prefix:
def build_prefix(arr):
    n = len(arr)
    prefix = [0] * n

    prefix[0] = arr[0]

    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]

    return prefix

# Code for range sum
def range_sum(prefix, L, R):
    if L == 0:
        return prefix[R]
    return prefix[R] - prefix[L-1]

# Interview Explaination:
'''Prefix sum stores cumulative totals so range queries can be 
answered in constant time. instead of recomputing sums repeatedly,
we preprocess once and use subtraction to obtain any subarray sum
instantly.'''
