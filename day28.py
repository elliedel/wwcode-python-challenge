'''
Day 28 - Create a program that removes the nth element from a list.
'''
list_to_use = []

def getNumber():
    while True:
        try:
            num = float(input())
            # if input doesn't have a floating point, it returns as an integer. else, retain as float
            return int(num) if num % 1 == 0.0 else num
        
        # If input is not a number, it will reprompt the question
        except ValueError:
            pass

def enterNumber(s):
    while True:
        try:
            for i in range(s):
                num = float(input("Enter a number: "))
                if num % 1 == 0.0:
                    list_to_use.append(int(num))
                else:
                    list_to_use.append(num)
            break
        # If input is not a number, it will reprompt the question
        except ValueError:
             pass

print("Enter size:",end=" ")
size = getNumber()
num = enterNumber(size)

print("",f"Before: {list_to_use}", sep="\n")
print("Enter the element number to remove:",end=" ")

nth = getNumber()
list_to_use.pop(nth-1) # since indexing starts at 0, decreasing it by one will access the nth element
print("",f"After: {list_to_use}", sep="\n")
