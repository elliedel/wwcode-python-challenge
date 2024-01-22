'''
Day 5 - Write a program to find the maximum and minimum values in a list.
'''
li = []

# Gets the size by asking input from the user while also evaluating if they entered a valid list size
def getSize():
    while True:
        try:
            s = int(input("Enter size of list: "))
            return s
        
        except ValueError:
            print("Must be an integer.")
            pass

# Asks each list elements while adding all of the elements together
def getValues(size):
    for i in range(size):
        while True:
            try:
                element = float(input(f"Enter value #{i+1}: "))
                li.append(int(element)) if element % 1 == 0.0 else li.append(element)
                break # Breaks the while loop if users enter a numerical value. Else, it will ask for the item value again

            except ValueError:
                pass

size = getSize()
getValues(size)

print("",f"Minimum Value: {min(li)}",f"Maximum Value: {max(li)}",sep="\n")
