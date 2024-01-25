
'''
day 15 - Create a program that checks if a year is a leap year.
'''
def enterYear():
    while True:
        try:
            year_to_check = int(input("Enter year: "))
            return year_to_check
        except ValueError:
            print("Please enter a valid year.", end="\n\n")
            pass

# As a general rule for leap years, a year must have either of these conditions to become a leap year
# [1] They must be divisble by 4
# [2] They musn't be divisible by 100, but can be considered a leap year if it is divisible by 400

def validateLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = enterYear()
isYear = validateLeapYear(year)
if isYear == True:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")