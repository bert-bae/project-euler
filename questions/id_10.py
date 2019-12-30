# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from utils.math_utils import *

def findSumOfPrimesBelow(num):
  sum = 0
  for i in range(1, num - 1):
    if isPrime(i):
      sum += i
      print(i)
  return sum

print(findSumOfPrimesBelow(2000000))