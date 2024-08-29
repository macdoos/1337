# O(N) time | O(1) space
def singleNumber(nums):
  xor = 0
  for num in nums:
      xor ^= num
  
  return xor

input = [2,2,1]
print(singleNumber(input))
