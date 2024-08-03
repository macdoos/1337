# O(N) time | O(1) space | recursion
def getNthFib(n):
  res = []

  if n == 2:
      return 1
  elif n == 1:
      return 0
  else:
      return getNthFib(n - 1) + getNthFib(n - 2)

input = 6
print(getNthFib(input)) # 0, 1, 1, 2, 3, 5
