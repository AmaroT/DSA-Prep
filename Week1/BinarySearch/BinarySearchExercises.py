#1 Binary Search: Efficient Searching in Sorted Data
# We need a sorted list (pre-condition)
# Initialize low (start) and high(end) pointers 
# Loop: Calculate mid, compare target to mid-element
# - If equal: Found!
# - If target < mid: Search left half(high = mid - 1)
# - If target > mid: Search right half (low = mid + 1)
# Loop ends when low > high (not found)
# This "halving" minimizes comparisons, like guessing a number between 1 - 100 in ~ 7 tries max. 

def binary_search(arr, target):
    low, high = 0, len(arr) - 1 # Pointers to search range
    while low <= high:          # While range is valid
        mid = (low + high) // 2 # Avoid overflow: integer division
        if arr[mid] == target:
            return mid          # Found: return index
        elif arr[mid] > target:
            high = mid - 1      # Shrink right
        else: 
            low = mid + 1       # Shrink left
    return - 1                  # Not found
    

print(binary_search([1, 3, 5, 7], 7))
print(binary_search([-1, 0, 1], -1))
print(binary_search([-5, -3, 0, 2], -3))
print(binary_search([-5, -3, 0, 2], -6))


# Why this structure? The while loop ensures we don't miss edges: mid-calc is safe/central; early return for success keeps it efficient. 

# Count Occurences: Modify to return how many times "target" appears (not just index). 
# Starter: After finding one, scan left/right from "mid" to count.