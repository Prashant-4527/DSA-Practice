# Problem : Check if an array is sorted in ascending order, descending order, or not sorted at all. Handle Strictly
# increasing vs non-decreasing too.

# Optimal Solutions: All Variants

# Variant 1: Check if sorted ascending (non-decreasing: allows equal)

def is_sorted_ascending(arr):
    if len(arr) <= 1:
        return True         # 0 or 1 element is always sorted
    
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:     # Current element SMALLER than previous?
            return False          # Violated! not sorted
        
    return True


# Variant 2: Check if strictly increasing (no equal element allowed)
def is_strictly_increasing(arr):
    if len(arr) <= 1:
        return True         # 0 or 1 element is always sorted
    

    for i in range(1 , len(arr)):
        if arr[i] <= arr[i-1]:  # Equal OR Smaller -> not strictly increasing
            return False
    
    return True


# Variant 3: Check if sorted descending (non-increasing)
def is_sorted_descending(arr):
    if len(arr) <=1:
        return True
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:   # Current BIGGER than previous? wrong for desc
            return False 
        
    return True



# Variant 4: ELITE - Chekc what kind od sorted it is
def check_sorted_type(arr):
    if len(arr) <=1:
        return "trivially sorted"
    
    ascending = True
    descending = True
    strict_asc = True

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            ascending = False
            strict_asc = False
        if arr[i] > arr[i-1]:
            descending = False
        if arr[i] == arr[i-1]:
            strict_asc = False

    if strict_asc:
        return "strictly increasing"
    elif ascending:
        return "non-decreasing (has duplicates)"
    elif descending:
        return "descending"
    else:
        return "not sorted"
    
# TIme: O(n), Space: O(1)

# Tests:
print(is_sorted_ascending([1, 2, 3, 4, 5]))    # True
print(is_sorted_ascending([1, 1, 2, 3]))        # True (equal allowed)
print(is_sorted_ascending([1, 3, 2, 4]))        # False

print(is_strictly_increasing([1, 2, 3, 4]))     # True
print(is_strictly_increasing([1, 1, 2, 3]))     # False (has equal)

print(is_sorted_descending([5, 4, 3, 2, 1]))    # True
print(is_sorted_descending([5, 5, 3, 2]))       # True (equal allowed)

print(check_sorted_type([1, 2, 3, 4]))          # "strictly ascending"
print(check_sorted_type([1, 1, 2, 3]))          # "non-decreasing (has duplicates)"
print(check_sorted_type([5, 4, 3]))             # "descending"
print(check_sorted_type([3, 1, 4, 2]))          # "not sorted"
print(check_sorted_type([7]))                   # "trivially sorted"


'''
First i'd clarify - sorted ascending or descending? Strictly increasing or non-descending? Once confirmed,I scan adjacent
pairs in one pass: For ascendind, if any element is less than its previous one, i return false. For descending, if any elemnet
is greater than previous. for strictly increasing, i return false on equal elements too.
One pass O(n)time, O(1)space. Edd=ge case: array is 0 or 1 elements are always considered sorted.
'''
