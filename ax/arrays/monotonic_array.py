# O(N) time | O(1) space | loop
def isMonotonic(array):
    isNonDec = True
    isNonInc = True
    N = len(array)
    for i in range(1, N):
        if array[i] > array[i - 1]:
            isNonDec = False
        if array[i] < array[i - 1]:
            isNonInc = False

    return isNonDec or isNonInc

input = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print(isMonotonic(input))
