'''
Day 29 - Create a function that generates a random number between a given range.
'''
from random import randint

# function that generates random number from a given range using randint function from random library
def generateRandNum(rang1, rang2):
    return randint(rang1,rang2)


while True:
    try:
        rang1 = int(input("Enter lowest value of the range: "))
        rang2 = int(input("Enter highest value of the range: "))
        break
    
    # rang1 and rang2 values will only take integer since the randint function does not take non-integer values
    except ValueError:
        print("You did not enter an integer.", "",sep="\n")

print("",f"Generated Number: {generateRandNum(rang1,rang2)}", sep="\n")