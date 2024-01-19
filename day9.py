'''
Day 9 - Write a program to check if a number is even or odd.

My solution, assuming that 0 is even.
'''
def numValidate():
    while True:
        try:
            num = int(input("Enter a number (must be an integer): "))
            return num
        except ValueError:
            print("You did not enter an integer.", end="\n\n")
            pass

def OddEvenChecker(num):
    if num % 2 == 0:
        return f"{num} is even."
    elif num % 2 != 0:
        return f"{num} is odd."
    
number = numValidate()
print(OddEvenChecker(number))