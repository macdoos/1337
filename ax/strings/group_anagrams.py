# O(NWlog(N)) time | O(NW) space | hashmap of sorted words
def groupAnagrams(words):
  anagrams = {}

  for w in words:
      sorted_word = ''.join(sorted(w))
      if sorted_word in anagrams:
          anagrams[sorted_word].append(w)
      else:
          anagrams[sorted_word] = [w]

  return list(anagrams.values())

input = ['yo', 'act', 'flop', 'tac', 'foo', 'cat', 'oy', 'olfp']
print(groupAnagrams(input))
