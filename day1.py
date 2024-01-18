'''
Day 1 - Create a program that swaps the values of two variables.
'''
val1 = input("Enter value of the first value: ")
val2 = input("Enter value of the second value: ")

print("","Before swapping: ", f"value 1: {val1}", f"value 2: {val2}",sep="\n",end="\n\n")

val1, val2 = val2, val1

print("After swapping: ", f"value 1: {val1}", f"value 2: {val2}",sep="\n")