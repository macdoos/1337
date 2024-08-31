# O(n) time | O(1) space
def removeElement(nums, val):
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] == val:
            nums[i], nums[n-1] = nums[n-1], nums[i]
            n -= 1
        else:
            i += 1
    return n

nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))
print(nums)
