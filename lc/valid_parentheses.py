# O(N) time | O(N) space
def valid_parentheses(s):
  lookup = {')':'(','}':'{',']':'['}
  stack = []

  for p in s:
      if p in lookup.values():
          stack.append(p)
      elif stack and lookup[p] == stack[-1]:
          stack.pop()
      else:
          return False

  return stack == []

input = '()'
print(valid_parentheses(input))
