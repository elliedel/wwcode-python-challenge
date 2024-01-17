'''
Python Days of Code - Day 7
Prompt: Write a program to check if a number is positive, negative, or zero.
'''
def enterNumber():
    while True:
        try:
            num = float(input("Enter a number: "))
            # if input doesn't have a floating point, it returns as an integer. else, retain as float
            return int(num) if num % 1 == 0.0 else num
        
        # If input is not a number, it will reprompt the question
        except ValueError:
            pass

num = enterNumber()
if num > 0:
    print(f"{num} is positive.")
elif num < 0 :
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")