'''
Day 3 - Write a function to count the number of vowels in a given string
'''
vowels = ["a", "e", "i", "o", "u"]

def vowelChecker(str):
    count = 0
    for s in str:
        if s.lower() in vowels:
            count+=1
    return count
            
str_to_check = input("Enter your string: ")
count = vowelChecker(str_to_check)
print(f"Number of vowels: {count}")