'''
Day 10 - Write a program to remove duplicates from a list.
'''

li = [
    "apple", "orange", "banana", "apple", "grape", "kiwi", 1, "orange", "pear", "kiwi", "banana", True, 1
    ]
eval = []

print(li, end="\n\n")

for i in range(len(li)):
    try:
        if li[i] in eval:
            print(f"del: {li[i]}, {i}")
            li.remove(li[i])
            i -= i
        else:
            print(f"save {li[i]}, {i}")
            eval.append(li[i])
    except IndexError:
        break
print(li)
