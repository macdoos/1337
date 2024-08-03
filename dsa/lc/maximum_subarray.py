# O(N) time | O(1) space
def maxSubArray(nums):
  cur = max_global = nums[0]
  N = len(nums)

  for i in range(1, N):
      cur = max(nums[i], cur + nums[i])

      if cur > max_global:
          max_global = cur

  return max_global

input = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(input))
