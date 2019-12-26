# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def getPrimeFactors(num):
  i = 2
  primes = []
  while num > 1:
    if (num % i) == 0:
      primes.append(i)
      num = (num / i)
    else:
      i += 1
  return primes

print(max(getPrimeFactors(600851475143)))