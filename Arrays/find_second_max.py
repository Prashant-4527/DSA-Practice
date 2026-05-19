Problem: Find Second largest element in array

# Approach:
1.two variables to hold largest and second largest.
2.compare with each element once.
3. if element > largest. current largest become second largest and largest will be update with element
4. if element is smaller than largest but greater than second largest so update the second largest with element

Time Complexity: o(n)
Space Complexity: O(1)

# Interview explaination:
'''I maintain two variables-- largest and second largest.
While scanning, if i find a new largest, I shift previous largest to second.
Otherwise if element lies between them and is distinct, i update second.
This requires one pass --- theta(n) time and constant space'''

Code:
def find_second_largest(arr):
    if not arr or len(arr) < 2:
        return None
    
    largest = float('-inf')
    second = float('-inf')

    for x in arr:
        if x > largest:
            second = largest
            largest = x
        elif largest > x > second:
            second = x

    # if second == float('-inf'):  # use this for duplicate handling
    #     return None

    return second
