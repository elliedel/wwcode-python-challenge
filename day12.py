'''
    Day 12: Write a program to reverse a given string.
'''

message = input("Enter a string: ")
reversed= "" # initialised reversed string variable

count = len(message)
for m in message:
    count -= 1
    reversed += message[count] # every loop decrements the count which is used for the index of the string message, and added to the reversed var

print("Reversed:", reversed)
