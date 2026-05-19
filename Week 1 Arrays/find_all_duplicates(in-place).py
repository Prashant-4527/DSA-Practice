# Problem: Find All Duplicates (In-place)

# Brute Force:
def find_duplicates_brute(arr):
    result = []
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num, count in freq.items():
        if count == 2:
            result.append(num)

    return result

# Time: O(n), Space: O(n)

# Optimal Approach:
'''
Key Idea: Array ki value ko INDEX ki tarh use karo.
          Value ko negative karna = "maine yha visit kiya" ka mark.

Step 1: For every element:
    Step 1a: Extract Index = abs(arr[i]) - 1
             (abs islite kyuki phele wala step
             already negative kar chuka hoga)
             (-1 isliye kyuki array 0-indexed hai
             but values 1 se start hoti hai)
    
    Step 1b: Us index me jaao: arr[index]
             agar arr[index] POSITIVE hai:
               -> pheli barr aa raha hai
               -> Use NEGATIVE karo 
             agar arr[index] NEGATIVE hai:
              -> phele aa chuka hai!
              -> Yeh Duplicate hai -> result me dalo

Step 2: Result return karo!
'''

# Code:
def find_duplicates(arr):
    result = []

    for i in range(len(arr)):
        index = abs(arr[i]) - 1


        if arr[index] < 0:
            result.append(abs(arr[i]))

        else:
            arr[index] = -arr[index]

    return result
# Time: O(n), Space: O(1)
# Test case:
print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))
print(find_duplicates([1, 2, 3, 4, 5, 1, 2]))

# Interviwe Explaination:
'''
Main values ko indcies ki tarah use karunga. har value ke liye, us index 
pe jata hoon aur negative mark karta hoon. agar already negative hai - duplicate
mil gya.
'''

