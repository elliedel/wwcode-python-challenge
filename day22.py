'''
Day 22 - Create a program to find the second-largest element in a list.
'''
list_to_use = []

def getSize():
    while True:
        try:
            s = float(input("Enter size: "))
            # if input doesn't have a floating point, it returns as an integer. else, retain as float
            return int(s) if s % 1 == 0.0 else s
        
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
        
size = getSize()
num = enterNumber(size)
reversedlist = list_to_use.copy()
reversedlist.sort(reverse=True)

print("",f"List: {list_to_use}",f"Second-largest Element: {reversedlist[1]}", sep="\n")

