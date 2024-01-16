'''
Python Days of Code - Day 6
Prompt: Write a program to count the occurrences of a specific character in a string.
'''

# function to validate if the input is a character
def charValidator():
    while True:
        char_to_check = input("Input the specific character to check: ")
        # if the input's length is 1, it returns the value, else it will reprompt the question
        if len(char_to_check) == 1:
            return char_to_check

def charChecker(str_to_check, char_to_check):
    count = 0
    for i in str_to_check:
        # if the character to check is the same as the character in the string, the count is increased
        if char_to_check == i:
            count+=1
    return count

str_to_check = input("Input a string: ")
char_to_check = charValidator()
print(f"\nThe occurence of '{char_to_check}' in the string : {charChecker(str_to_check, char_to_check)}")



