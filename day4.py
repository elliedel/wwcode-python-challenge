'''
Day 4 - Write a program to find the sum of all elements in a list.
'''
li = []
sum = 0

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
def getSum(size, sum):
    for i in range(size):
        while True:
            try:
                element = float(input(f"Enter value #{i+1}: "))
                # If element is a float, it appends it to the list as is. Else, it'll be appended as an integer.
                if element % 1 == 0.0:
                    li.append(int(element))
                    sum += element
                else:
                    li.append(element)
                    sum += element
                break

            # If wrong datatype (String, etc.), it will prompt for the index value again
            except ValueError:
                pass
    return int(sum) if sum % 1 == 0.0 else sum

size = getSize()
sum = getSum(size, sum)
print("",f"List: {li}",f"Sum: {sum}",sep="\n")
