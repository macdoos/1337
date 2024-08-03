# O(N^2) time | O(1) space | iterative swaps
def bubbleSort(array):
  is_sorted = False
  counter = 0
  N = len(array) - 1

  while not is_sorted:
      is_sorted = True
      for i in range(N - counter):
          if array[i] > array[i + 1]:
              array[i], array[i + 1] = array[i + 1], array[i]
              is_sorted = False
      counter += 1

  return array

input = [8, 5, 2, 9, 5, 6, 3]
print(bubbleSort(input))
