'''
    Day 12: Write a program to reverse a given string.
'''
import time

message = input("Enter a string: ")
reversed= ""

count = len(message)
for m in message:
    count -= 1
    reversed += message[count]

print("Reversed: ",reversed)
