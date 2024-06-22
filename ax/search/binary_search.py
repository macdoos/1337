# O(logN) time | O(1) space | two pointers
def binarySearch(array, target):
  left = 0
  right = len(array) - 1

  while left <= right:
      middle = (left + right) // 2
      match = array[middle]

      if match == target:
          return middle
      elif target > match:
          left = middle + 1
      else:
          right = middle - 1

  return -1

input = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
print(binarySearch(input, target))
