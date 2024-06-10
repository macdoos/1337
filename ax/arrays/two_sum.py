# O(N) time | O(N) space
def twoNumberSum(array, targetSum):
    N = len(array)
    nums = {}

    for num in array:
        diff = targetSum - num
        if diff in nums:
            return [diff, num]
        else:
            nums[num] = True

    return []

input = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
print(twoNumberSum(input, target))
