# O(N) time | O(1) space | iterative (two pointers)
def isPalindrome(string):
  left = 0
  right = len(string) - 1

  while left < right:
      if string[left] != string[right]:
          return False
      left += 1
      right -= 1

  return True

input = "abcdcba"
print(isPalindrome(input))
