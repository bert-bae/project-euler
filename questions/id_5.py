# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

divisors = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

def isDivisibleBy(num, division):
  return True if num % division == 0 else False

def findDivisibleTarget(arrMatch):
  maxNum = max(arrMatch)
  current = maxNum * 2
  state = False
  while state == False:
    result = True
    for i in arrMatch:
      if isDivisibleBy(current, i) is False:
        current += maxNum
        result = False
        break
    if result == True:
      state = True
  return current

print(findDivisibleTarget(divisors))