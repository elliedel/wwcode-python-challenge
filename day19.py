'''
Day 19 - Write a function to calculate the factorial of a number.
'''

def getNumber():
  while True:
    try:
      num = int(input("Enter number: "))
      return num
    except ValueError:
      pass

def getFactorial(n):
  factorial = 1
  for i in range(n,0,-1):
    factorial *= i
  return factorial

number = getNumber()
print(f"{number}! =", getFactorial(number))

