'''
Day 14 - Write a program to print the first n numbers of a Fibonacci sequence.
'''
def getNumber():
    while True:
        try:
            n = int(input("Enter n: "))
            return n
        
        except ValueError:
            print("Enter an integer.", end="\n\n")

def getFirstFibonacciNum(n):
    a,b = 1, 0  # initialise variables to store the two nearest previous sequence numbers
    print("", "Fibonnacci Sequence: ", end="", sep="\n")
    for i in range(n):
        seq_num = a + b   # adds the two nearest previous sequence numbers to get the current one
        print(f"{seq_num}", end=" ")

        a,b = b, seq_num

number = getNumber()
getFirstFibonacciNum(number)