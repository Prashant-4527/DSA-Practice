# Alogirithm:
'''
1. create two veriabls to store indexs left and right
2. left = 0
3. right = len(array)-1
4. using while loop where while left < right
5. swap the elements
6.add one in left and minus one in right
'''

# Code:

def reverse_array(arr):
    if not arr:
        return None
    
    left = 0
    right = len(arr)-1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1




    return arr

# Interview explaination:
'''I use pointers at opposite ends and swap elemnets while moving inwards
This performs n/2 swaps, giving theta(n) time.
Since reversal happens inside original array without extra storage,
auxiliary space is theta(1)'''
