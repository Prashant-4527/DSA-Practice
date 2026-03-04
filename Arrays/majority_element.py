# Approach:
'''
1.if count = 0 --> choose new candidate
2.if current element =  candidate -->count++
3.else-->count--
'''

# Time complexity: O(n)
# Space complexity: O(1)

# Code:
def majority_element(arr):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
        if num == candidate:
            count+=1
        else:
            count-=1

    # verification step
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return None

# Interview Explanation:
'''Since the majority element appears more than half the time, it
cannot be fully cancelled when pairing diffrent elements. the boyer-
moore algorithm tracks a candidate and cancels opposing elements.
the survivng candidate is then verified.'''
