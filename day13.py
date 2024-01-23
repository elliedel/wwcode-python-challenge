'''
Day 13 - Write a program to shuffle the elements of a list randomly.
'''
from random import shuffle
li = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie"]

print("Original List:", li, sep="\n", end="\n\n")
shuffle(li)

print("Shuffled List:", li, sep="\n")