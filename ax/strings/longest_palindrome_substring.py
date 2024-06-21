# O(N^2) time | O(N) space | middle out / two pointers
def longestPalindromicSubstring(string):
  current_longest = [0, 1]
  for i in range(1, len(string)):
      odd = get_longest_palindrome_from(string, i - 1, i + 1) # i.e. aba
      even = get_longest_palindrome_from(string, i - 1, i) # i.e. abba
      longest = max(odd, even, key = lambda x: x[1] - x[0])
      current_longest = max(longest, current_longest, key = lambda x: x[1] - x[0])
  return string[current_longest[0]:current_longest[1]]

def get_longest_palindrome_from(string, left, right):
  while left >= 0 and right < len(string):
      if string[left] != string[right]:
          break
      left -= 1
      right += 1
  return [left + 1, right]

input = 'abaxyzzyxf'
print(longestPalindromicSubstring(input))
