'''
Day 11 - Write a program to print the multiplication table of a given number.
'''

def validateNumber():
    while True:
        try:
            n = int(input("Enter a number: "))
            return n
        
        except ValueError:
            print("")
            pass

number = validateNumber()
for i in range(1,11):
    print(f"{number} x {i} = {number*i}",sep="\n")