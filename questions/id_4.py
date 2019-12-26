
import math

def checkPalindrome (input):
  half = math.floor(len(input) / 2)
  for char in range(0, int(half)):
    if input[char] != input[len(input) - 1 - char]:
      return False
  return True

def getLargestPalindrome():
  result = None
  for x in reversed(range(100, 999)):
    for y in reversed(range(100, 999)):
      if checkPalindrome(str(x * y)):
        if (x * y) > result:
          result = x * y
        break
  return result

print(getLargestPalindrome())