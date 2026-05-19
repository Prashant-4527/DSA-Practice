# Problem: Majority Element > n/2 (Boyer-Moore Voting)

# Brute Force Approach:
def majority_brute(arr):
    n = len(arr)
    for num in arr:
        count = arr.count(num)
        if count > n//2:
            return num
    return -1
# Time: O(n^2), Space: O(n)

# Optimal Approach:

# Algorithm:
'''
Step 1: Do variables bnao:
        candinate = None
        count = 0

Step 2: For Each element:
        if count = 0:
            -> New candinate! current element ko
            candinate bano

        if current element = candinate:
            -> Same team! count + 1 karo(support mila)
        if current element != candinate:
            -> Enemy! count - 1 karo (cancel out)

Step 3: Jo candinate bacha - woh majority element hai     
'''
# Code:
def majority_element(arr):
    candinate = None
    count = 0

    for num in arr:
        if count == 0:
            candinate = num
        if num == candinate:
            count +=1
        else:
            count -=1
    return candinate

# TimeL O(n), Space: O(1)

# Interview Explaination:
'''I'll use boyer-moore voting alogrithm. i'll track a candinate and a count.
If count == 0 set a new candinate. if same element count+=1 else count-=1.
in the end we will get the majority element in O(n) time and in O(1) Space'''