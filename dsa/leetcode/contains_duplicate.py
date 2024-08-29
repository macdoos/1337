def containsDuplicate(nums):
  lookup = set()

  for num in nums:
      if num in lookup:
          return True
      lookup.add(num)   
  return False

input = [1,2,3,1] 
print(containsDuplicate(input))
