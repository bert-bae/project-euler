import math

def isPrime(num):
  if num < 2:
    return False
  if num == 2:
    return True
  if num % 2 == 0:
    return False
  for i in range(3, int(math.floor(math.sqrt(num))), 2):
    if num % i == 0:
      return False
  return True