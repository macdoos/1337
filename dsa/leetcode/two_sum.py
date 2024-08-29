# O(N) time | O(N) space
def two_sum(nums, target):
    lookup = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in lookup:
            return [i, lookup[diff]]
        lookup[num] = i

input = [2, 7, 11, 15]
target = 9

print(two_sum(input, target))
