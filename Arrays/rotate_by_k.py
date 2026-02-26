# Problem: Rotate a array by k

# Approach:
1. Start pointer
2. End pointer
3. swap pointer
4. move inward
5. repeat until meet

# Code:

def reverse(arr, start, end):
  while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start +=1
    end-=1

def rotate_right_by_k(arr, k):
  n = len(arr)
 if n == 0:
   return arr

  k = k % n

  reverse(arr, 0, n-1)
  reverse(arr, 0, k-1)
  reverse(arr, k, n-1)

  return arr




    
