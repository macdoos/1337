# O(N) time | O(min(N, A)) space | enumerate into hashmap
def longestSubstringWithoutDuplication(string):
  last_seen = {}
  longest = [0, 1]
  start = 0

  for i, c in enumerate(string):
      if c in last_seen:
          start = max(start, last_seen[c] + 1)
      if longest[1] - longest[0] < i + 1 - start: # i + 1 - stat = potential match
          longest = [start, i + 1]
      last_seen[c] = i # add char to hashmap

  return string[longest[0]:longest[1]]

input = 'clementisacap'
print(longestSubstringWithoutDuplication(input))
