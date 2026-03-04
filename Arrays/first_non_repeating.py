# Approach:
'''
1.Build freq dict
2.traverse array from start
3.if freq[x]==1 --> return element
4.if none found ---> return none
'''

# Time Complexity: O(n)
# Space Complexity: O(n)

# Code:

def first_non_repeating(arr):
    if not arr:
        return None
    
    freq = {}

    for x in arr:
        freq[x] = freq.get(x, 0)+1

    for num in arr:
        if freq[x] == 1:
            return x
    
    return None


# Interview Explaintion:
'''To find the first non-repeating element, i first count frequencies using hasing, Then i scan the array
again to preserve order and return the first element whose frequency is one.'''
