# Approach:
'''
1.Create empty dictionary
2.Traverse array
3.if element exist --> increament count
4.else --> set count = 1
5.return dictionary 
'''

# Time Complexity: O(n)
# Space Complexity: O(n)

# Code:
def count_elemnt(arr):
    if not arr:
        return 0
    
    freq = {}

    for x in arr:
        if x in freq:
            freq[x]+=1
        else:
            freq[x]=1
    return freq

# Interview Explaination:
'''To count elements frequencies effciently, i use hasing. i traverse the array once and map
each value to its cocurrence count. This avoids repated scanning an reducing time complexity from 
quadratic to linear.'''
