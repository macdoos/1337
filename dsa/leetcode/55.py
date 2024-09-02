# O(n) time | O(1) space
def canJump(nums):
    max_jump = 0

    for i in range(len(nums)):
        if i > max_jump:
            return False
        max_jump = max(max_jump, i + nums[i])
        if max_jump >= len(nums) - 1:
            return True
    return True

nums = [2,3,1,1,4]
print(canJump(nums))
