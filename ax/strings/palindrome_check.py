def isPalindrome(string):
  r = reversed(string)

  return string == ''.join(r)

input = "abcdcba"
print(isPalindrome(input))
