# Algorithm:
'''
1.Create empty set --> seen
2.create empty list --> duplicate
3.Traverse array
4.if element in seen --> add to duplicates
5.else --> add to seen
'''


# Time Complexity: O(n)
# Space Complexity: O(n)


# Code:
def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for x in arr:
        if x in seen:
            duplicates.add(x)
        else:
            seen.add(x)
    return list(duplicates)

# Interview Explaination: 
'''To detect duplicates effciently, i track previously seen elemnts using a hash set. if an element appreas
again, it is a duplicate. This reduces time complexity from quadratic comparison to linear time.'''
