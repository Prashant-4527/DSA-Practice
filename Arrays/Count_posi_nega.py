# Problem: Count Positive , Negative and Zeros from array

# Approach: 
1. Two Vairables positive and negative to store the counts
2. compare each element with conditions
3. if element is larger than 0 then count in positive 
4. if smaller than 0 then count in negative
5. if equals to 0 then count in zero

# Code:
 def count_nega_posi_zero(arr):
   if not arr:
     return 0, 0, 0

  positive. negative, zero = 0, 0, 0

  for x in arr:
    if x > 0:
      positive+=1
    elif x < 0:
      negative+=1
    elif x == 0:
      zero+=1

  return positive, negative, zero 

# Interview Explaination:
''' I Performe a single linear scan and classify each element based on its sign.
since each element is examined once, time complexity is O(n) and only constant counters are maintained, so auxiliary space is O(1).'''
