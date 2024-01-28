'''
    Day 18 - Create a program to find the largest among three numbers.
'''
def getThreeNumbers():
    while True:
        try:
            num1 = float(input("Enter number 1: "))
            num2 = float(input("Enter number 2: "))
            num3 = float(input("Enter number 3: "))
            return num1, num2, num3
        
        except ValueError:
            print("You did not enter a valid number.",end="\n\n")
            pass

# Changing to int if numbers are int. Else, it stays as float.
def changeAppropriateType(num1, num2, num3):
    if num1 % 1 == 0:
        num1 = int(num1)
    if num2 % 1 == 0:
        num2 = int(num2)
    if num3 % 1 == 0:
        num3 = int(num3)
    return num1, num2, num3

number1, number2, number3 = getThreeNumbers()
number1, number2, number3 = changeAppropriateType(number1, number2, number3)

print("",f"Values: {number1}, {number2}, {number3}",f"Largest Number: {max(number1, number2, number3)}", sep="\n")