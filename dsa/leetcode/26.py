# O(n) time | O(1) space
def removeDuplicates(nums):
    n = len(nums)
    j = 1

    for i in range(1, n):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1
    return j

nums = [1,1,2]
print(removeDuplicates(nums))
print(nums)
