# O(N) time | O(1) space
def isPowerOfFour(n):
    if n <= 0:
        return False
    while n != 1:
        if n % 4 != 0:
            return False
        n = n // 4
    return True

input = 16
print(isPowerOfFour(input))
