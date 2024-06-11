# O(N) space | O(1) time | two pointers
def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    N = len(array)

    while arrIdx < N and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1

    return seqIdx == len(sequence)

input = [5, 1, 22, 25, 6, -1, 8, 10]
seq = [1, 6, -1, 10]
print(isValidSubsequence(input, seq))
