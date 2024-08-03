# O(N) time | O(1) space | two pointers
def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1

    while left < right:
        while left < right and array[right] == toMove:
            right -= 1
        if array[left] == toMove:
            array[left], array[right] = array[right], array[left]
        left += 1

    return array

input = [2, 1, 2, 2, 2, 3, 4, 3]
target = 2
print(moveElementToEnd(input, target))
