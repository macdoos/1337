# O(N^2) time | O(1) space | iterative swaps of smallest index
def selectionSort(array):
  current = 0
  while current < len(array) - 1:
      smallest = current
      for i in range(current + 1, len(array)):
          if array[smallest] > array[i]:
              array[smallest], array[i] = array[i], array[smallest]
      current += 1

  return array

input = [8, 5, 2, 9, 5, 6, 3]
print(selectionSort(input))

