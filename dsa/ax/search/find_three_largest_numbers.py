# O(N) time | # O(1) space | array shifting
def findThreeLargestNumbers(array):
  largest = [float('-inf')] * 3

  for num in array:
      if num > largest[2]:
          largest = [largest[1], largest[2], num]
      elif num > largest[1]:
          largest = [largest[1], num, largest[2]]
      elif num > largest[0]:
          largest = [num, largest[1], largest[2]]

  return largest

input = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNumbers(input))
