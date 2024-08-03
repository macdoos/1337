# O(N) time | O(1) space
def lengthOfLastWord(s):
  arr = s.split()
  return len(arr[-1])

input = 'Hello World'
print(lengthOfLastWord(input))
