'''
Day 21 - Create a program to remove a specific element from a set.
'''
list_to_use = ["sparkling", "effervescent", "whimsical", "resilient", "serene", "mysterious", "captivating", "exuberant", "intriguing", "vibrant"]

while True:
    print(f"LIST BEFORE: {list_to_use}")

    try:
        i_remove = input("Enter the element value or index to remove: ")
        if i_remove.isalpha() == True: # if user enters a number, it uses the remove function to remove the item value
            list_to_use.remove(i_remove)
            break
        
        elif i_remove.isdigit() == True: # if it's a number, it uses the del() function
            del(list_to_use[int(i_remove)])
            break
    
    # in case the user enters invalid inputs (wrong item value, wrong index, etc.)
    except ValueError:
        print("Invalid input...", end = "\n")
        pass
    except IndexError:
        print("Invalid input...", end = "\n")
        pass

print("",f"LIST AFTER: {list_to_use}",sep="\n")
