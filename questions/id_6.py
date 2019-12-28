# The sum of the squares of the first ten natural numbers is, 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)2 = 552 = 3025

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def squareSumToTarget(num):
  sum = 0
  for i in range(1, num + 1):
    sum += (i ** 2)
  return sum

def sumThenSquare(num):
  sum = 0
  for i in range(1, num + 1):
    sum += i
  return sum ** 2

def getDifference(numA, numB):
  return abs(numA - numB)

print(getDifference(
  squareSumToTarget(100),
  sumThenSquare(100)
))