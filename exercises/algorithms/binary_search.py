# Write a recursive function, `binarySearch(sortedArray, target)`, that returns
# the index of `target` in `sortedArray`, or -1 if it is not found. Do NOT use
# the built-in `Array.prototype.indexOf` or `Array.prototype.includes` methods 
# in your implementation.

# Here's a quick summary of the binary search algorithm:

# Start by looking at the middle item of the array. If it matches the target,
# return its index. Otherwise, recursively search either the left or the right
# half of the array until the target is found or the base case (empty array) is
# reached.

def binary_search(nums, target):
    if not nums:
        return -1

    mid = len(nums) // 2
    if nums[mid] > target: 
        return binary_search(nums[:mid], target)
    elif nums[mid] < target:
        right = binary_search(nums[mid + 1:], target)
        return -1 if right == -1 else right + mid + 1
    else:
        return mid

print(binary_search([1, 4, 7, 8, 10, 14, 16, 20, 25], 20))