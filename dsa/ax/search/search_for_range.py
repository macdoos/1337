# O(logN) time | O(1) space | iterative binary search with two pointers
def searchForRange(array, target):
  final_range = [-1, -1]
  right = 0
  left = len(array) - 1

  # Find the leftmost index
  left, right = 0, len(array) - 1
  while left <= right:
      mid = (left + right) // 2
      if array[mid] < target:
          left = mid + 1
      elif array[mid] > target:
          right = mid - 1
      else:
          if mid == 0 or array[mid - 1] != target:
              final_range[0] = mid
              break
          else:
              right = mid - 1

  # Find the rightmost index
  left, right = 0, len(array) - 1
  while left <= right:
      mid = (left + right) // 2
      if array[mid] < target:
          left = mid + 1
      elif array[mid] > target:
          right = mid - 1
      else:
          if mid == len(array) - 1 or array[mid + 1] != target:
              final_range[1] = mid
              break
          else:
              left = mid + 1

  return final_range

input = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
target = 45
print(searchForRange(input, target))
