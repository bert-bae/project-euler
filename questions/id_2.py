# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def filterEvenNum (numArr):
  if numArr % 2 == 0:
    return True
  else:
    return False

def fibonacciSum (filterLogic):
  fibNumbers = [0, 1]
  nextNum = 0
  while nextNum <= 4000000:
    nextNum = fibNumbers[len(fibNumbers) - 2] + fibNumbers[len(fibNumbers) - 1]
    fibNumbers.append(nextNum)

  return sum(filter(filterLogic, fibNumbers))

print(fibonacciSum(filterEvenNum))
