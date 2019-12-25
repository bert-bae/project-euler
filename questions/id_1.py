# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def sumOfMultiples(numA, numB, maxTarget):
  multiplier = 1
  sum = 0
  while multiplier < maxTarget:
    isValidNumA = multiplier % numA == 0
    isValidNumB = multiplier % numB == 0
    if isValidNumA & isValidNumB:
      sum += multiplier
    elif isValidNumA:
      sum += multiplier
    elif isValidNumB:
      sum += multiplier
    multiplier += 1
  print(f'This is the sum of the multiples of {numA} and {numB} up to multiplier # of {maxTarget} = {sum}')
  return multiplier


sumOfMultiples(3, 5, 1000)  