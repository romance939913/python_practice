# Write an `mergeSort` method that merge sorts an array. It
# should take an optional callback that compares two elements, returning -1 if 
# the first element should appear before the second, 0 if they are equal, and 1 
# if the first element should appear after the second. Define and use a helper 
# method, `merge(left, right, comparator)`, to merge the halves. 
#
# **IMPORTANT: Make sure to use a function declaration (`function merge`) as
# opposed to a function expression (`const merge = function`) for `merge`. Do
# NOT use the built-in `sort` method in your implementation.**
#
# Here's a summary of the merge sort algorithm:
#
# Split the array into left and right halves, then merge sort them recursively
# until a base case is reached. Use a helper method, merge, to combine the
# halves in sorted order, and return the merged array.

func = lambda left, right: 0 if left <= right else 1

def merge_sort(nums, func):
    if not nums:
        return nums

    mid = len(nums) // 2
    sorted_left = merge_sort(nums[:mid], func)
    sorted_right = merge_sort(nums[mid:], func)
    return merge(sorted_left, sorted_right, func)

def merge(left, right, comparator):
    answer = []

    while len(left) and len(right):
        if comparator(left[0], right[0] == 0):
            answer.append(left.pop(0))
        else:
            answer.append(right.pop(0))

    answer += left
    answer += right
    return answer