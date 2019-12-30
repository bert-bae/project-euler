# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

from utils.math_utils import isPrime

def getNthPrime(num):
  checked = [2, 3]
  counter = 4
  while len(checked) < num:
    if isPrime(counter) == True:
      checked.append(counter)
    counter += 1
  return max(checked)

print(getNthPrime(10001))
    