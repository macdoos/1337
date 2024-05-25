def two_sum(nums, target):
  lookup = {}
  N = len(nums)

  for i in range(N):
    if nums[i] in lookup:
      return [lookup[nums[i]], i]
    else:
      lookup[target-nums[i]] = i

  return None

input = [2, 7, 11, 15]
target = 9

print(two_sum(input, target))
