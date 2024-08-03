# O(N) time | O(N) space | recursive
def spiralTraverse(array):
    output = []
    fill(array, 0, len(array) - 1, 0, len(array[0]) - 1, output)
    return output

def fill(array, start_row, end_row, start_col, end_col, output):
    if start_row > end_row or start_col > end_col:
        return

    for col in range(start_col, end_col + 1):
        output.append(array[start_row][col])

    for row in range(start_row + 1, end_row + 1):
        output.append(array[row][end_col])

    for col in reversed(range(start_col, end_col)):
        if start_row == end_row:
            break
        output.append(array[end_row][col])

    for row in reversed(range(start_row + 1, end_row)):
        if start_col == end_col:
            break
        output.append(array[row][start_col])

    fill(array, start_row + 1, end_row - 1, start_col + 1, end_col - 1, output)

input = [
  [1, 2, 3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10, 9, 8, 7],
]

print(spiralTraverse(input))
