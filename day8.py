'''
Day 8 - Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.
'''
message = input("Enter your string: ")

up, low = 0, 0 # counter for occurences of uppercase and lowercase
for i in message:
    if i == i.upper() and i.isalpha():
        up+= 1
    elif i == i.lower() and i.isalpha():
        low+= 1
    # if it is neither uppercase or lowercase and not an alphabet, it will skip the count
    else:
        pass
print(f"Number of uppercase: {up}",f"Number of lowercase: {low}",sep="\n")