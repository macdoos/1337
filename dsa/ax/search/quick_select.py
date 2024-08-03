# O(N) time | O(1) space | itereative quicksort + position
def quickselect(array, k):
  start = 0
  end = len(array) - 1
  stack = [(start, end)]

  while stack:
      start, end = stack.pop()
      if start >= end:
          continue

      pivot = start
      left = start + 1
      right = end

      while left <= right:
          if array[left] > array[pivot] and array[right] < array[pivot]:
              array[left], array[right] = array[right], array[left]
          if array[left] <= array[pivot]:
              left += 1
          if array[right] >= array[pivot]:
              right -=1

      array[pivot], array[right] = array[right], array[pivot]
      left_subarray_is_smaller = right - 1 - start < end - (right + 1)

      if left_subarray_is_smaller:
          stack.append((start, right - 1))
          stack.append((right + 1, end))
      else:
          stack.append((right + 1, end))
          stack.append((start, right - 1))

  return array[k-1]

input = [8, 5, 2, 9, 5, 6, 3]
k = 3
print(quickselect(input, k))
