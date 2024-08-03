# O(logN) time | O(1) space | iterative with two pointers
def shiftedBinarySearch(array, target):
  left = 0
  right = len(array) - 1

  while left <= right:
      middle = (left + right) // 2
      match = array[middle]
      left_num = array[left]
      right_num = array[right]

      if target == match:
          return middle
      elif left_num <= match:
          if target >= left_num and target < match:
              right = middle - 1
          else:
              left = middle + 1
      else:
          if target <= right_num and target > match:
              left = middle + 1
          else:
              right = middle - 1

  return -1

input = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33
print(shiftedBinarySearch(input, target))
