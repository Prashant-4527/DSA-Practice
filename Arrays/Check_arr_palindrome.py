# Problem: Check Array is palindrome

# ApproacH:
1. left start from 0
2. right pointer start from len(arr)-1
3. while left < right
4. compare values
5. If diffrent not palindrome
6. move inward
7. if loop finishes --> palindrome

# Code:

def is_palindrome(arr):
  if len(arr) < 2 or not arr:
    return True

  left = 0
  right = len(arr) - 1

  while left < right:
    if arr[left] != arr[right]:
      return False
    left +=1
    right -=1

  return True


# Interview Explaination:
'''  A Palindrome has mirror symmetry.
I Use two pointers from both ends and compare elements.
if any mismatch occurs. it is not palindrome.
if all mirrored pairs match, it is palindrome.'''
