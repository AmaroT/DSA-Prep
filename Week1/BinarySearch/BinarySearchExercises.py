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

# def count_occurrences(arr, target):
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
# print(count_occurrences([1, 1, 2, 3, 5], 1))

def count_occurrences(arr, target): 
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
print(count_occurrences([1, 1, 2, 3, 5], 1)) # output: 2
print(count_occurrences([1, 3, 5, 7], 5)) # output: 1
print(count_occurrences([2, 2, 2, 3], 2)) #output: 3

# Exercise 3 - First Occurence(Leftmost Duplicate Finder)
# Given sorted "arr" and "target" , return the lowest index where "target" appears. If not found, -1.
# Example: arr = [1,2,2,2,3], target = 2, Return -> 1(not 2 o 3- the leftmost)
# Why this variant? Basic binary might return any index(e.g., middle 2). To bias left, we tweak the shrink logic: When equal, don't stop-peek left more (set high = mid, not break). This "hugs the left edge" of duplicates. 
# Starter Code(Build on your binary template - paste into a new func like "first_occurrence(arr,target)"):

def first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            # Don't return yet-check if there's one left-er
            high = mid - 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    # After loop: low is the first spot (if exists)
    if low < len(arr) and arr[low] == target:
        return low
    return -1

# Test
print(first_occurrence([1,2,2,2,3], 2)) # 1
print(first_occurrence([1,3,5], 3))     # 1
print(first_occurrence([1,2,3], 0))     # -1

