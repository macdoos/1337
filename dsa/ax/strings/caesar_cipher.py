# O(N) time | O(N) space | Modulo operator
def caesarCipherEncryptor(string, key):
  newLetters = []
  newKey = key % 26

  for x in string:
      newLetters.append(getNewLetter(x, newKey))
  return "".join(newLetters)

def getNewLetter(letter, key):
  newLetterCode = ord(letter) + key
  return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

input = 'xyz'
key = 2
print(caesarCipherEncryptor(input, key))
