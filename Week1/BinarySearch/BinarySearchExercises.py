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

# def count_occurances(arr, target):
#     low, high = 0, len(arr) - 1
#     target_count = 0
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             if target_count == target:
#                 target_count + 1
#                 return mid
#         elif arr[mid] > target:
#                 high = mid - 1
#         else:
#                 low = mid + 1
#                 return - 1
# print(count_occurances([1, 1, 2, 3, 5], 1))

def count_occurences(arr, target): 
    low,high = 0, len(arr) -1
    found_idx = -1      # Track where its found
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            found_idx = mid # Found one-note index, but DON'T return yet!
            break # Exit loop early (optional-saves time, but full loop also fine)
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    # Step 2: Count left duplicates
    count = 1 # The one that we found
    # Scan left: i decreases while == target
    if found_idx == -1: 
        return 0
    i = found_idx -1  # Start *just left* of found: i = 0 - 1 = -1
    while i >= 0 and arr[i] == target: # Check: In bounds *and* matches?
        count += 1 # Tally this extra!
        i -= 1     # Step left (decrement index)

    i = found_idx + 1 # Start *just right* of found: i = 0 + 1 = 1
    while i >= 0 and arr[i] == target: # Check: In Bounds *and* matches?
        count += 1 # Tally this extra!
        i += 1      # Step right (increment index)
    return count
    

# Test it
print(count_occurences([1, 1, 2, 3, 5], 1)) # output: 2
print(count_occurences([1, 3, 5, 7], 5)) # output: 1
print(count_occurences([2, 2, 2, 3], 2)) #output: 3