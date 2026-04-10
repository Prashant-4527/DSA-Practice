# ============================================================
# DSA TRAINING EVERYDAY
# Week 2 - Day 1 | Two Pointers
# Problems: Two Sum Sorted, Remove Duplicates, Remove Element
# GitHub: github.com/Prashant-4527
# ============================================================


# ------------------------------------------------------------
# Problem 1: Two Sum - Sorted Array
# Given a sorted array and target, find two numbers that sum
# to target. Return their 1-based indices.
#
# Time:  O(n)
# Space: O(1)
# Pattern: Two Pointers - shrink from both ends
# ------------------------------------------------------------

def two_sum_sorted(arr: list[int], target: int) -> list[int]:
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left + 1, right + 1]   # 1-based index

        elif current_sum > target:
            right -= 1    # sum too big → move right inward

        else:
            left += 1     # sum too small → move left inward

    return []   # no pair found


# ------------------------------------------------------------
# Problem 2: Remove Duplicates from Sorted Array
# Remove duplicates in-place. Return count of unique elements.
#
# Time:  O(n)
# Space: O(1)
# Pattern: Two Pointers - slow/fast, slow writes on new value
# ------------------------------------------------------------

def remove_duplicates(arr: list[int]) -> int:
    if not arr:
        return 0

    slow = 1

    for fast in range(1, len(arr)):
        if arr[fast] != arr[fast - 1]:   # new unique value found
            arr[slow] = arr[fast]
            slow += 1

    return slow


# ------------------------------------------------------------
# Problem 3: Remove Element
# Remove all occurrences of val in-place.
# Return count of remaining elements.
#
# Time:  O(n)
# Space: O(1)
# Pattern: Two Pointers - slow writes when element != val
# ------------------------------------------------------------

def remove_element(arr: list[int], val: int) -> int:
    slow = 0

    for fast in range(len(arr)):
        if arr[fast] != val:       # keeper found
            arr[slow] = arr[fast]
            slow += 1

    return slow


# ------------------------------------------------------------
# Test Cases
# ------------------------------------------------------------

if __name__ == "__main__":

    # Two Sum Sorted
    print("=== Two Sum Sorted ===")
    print(two_sum_sorted([2, 7, 11, 15], 9))      # [1, 2]
    print(two_sum_sorted([1, 3, 4, 7, 9], 11))    # [3, 4]
    print(two_sum_sorted([1, 2, 3, 4], 8))        # []

    # Remove Duplicates
    print("\n=== Remove Duplicates ===")
    arr1 = [1, 1, 2, 3, 3, 4]
    k = remove_duplicates(arr1)
    print(k, arr1[:k])                             # 4 [1, 2, 3, 4]

    arr2 = [1, 1, 1, 1]
    k = remove_duplicates(arr2)
    print(k, arr2[:k])                             # 1 [1]

    arr3 = [1, 2, 3]
    k = remove_duplicates(arr3)
    print(k, arr3[:k])                             # 3 [1, 2, 3]

    # Remove Element
    print("\n=== Remove Element ===")
    arr4 = [3, 2, 2, 3]
    k = remove_element(arr4, 3)
    print(k, arr4[:k])                             # 2 [2, 2]

    arr5 = [0, 1, 2, 2, 3, 0, 4, 2]
    k = remove_element(arr5, 2)
    print(k, arr5[:k])                             # 5 [0, 1, 3, 0, 4]

    arr6 = [2, 2, 2]
    k = remove_element(arr6, 2)
    print(k, arr6[:k])                             # 0 []
