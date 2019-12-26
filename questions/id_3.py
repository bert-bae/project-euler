# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def getFactors(num):
  i = 2
  factors = []
  while num > 1:
    if (num % i) == 0:
      factors.append(i)
      num = (num / i)
    else:
      i += 1
  return factors

def checkSetForPrime(num):
  if num < 2:
    return False
  if num == 2:
    return True
  for i in range(3, num):
    if num % i == 0:
      return False
  return True

print(getFactors(600851475143))
print(max(filter(checkSetForPrime, getFactors(600851475143))))