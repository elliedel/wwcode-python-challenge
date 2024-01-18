'''
Day 2 - Create a program to calculate the area of a circle given its radius.

'''
from math import pi

def getValidInput():
    while True:
        try:
            r = float(input("Radius: "))
            return r
        except ValueError:
            pass

def areaCircle(radius):
    area = pi * (radius**2)
    return area

radius = getValidInput()
print(f"Area of a Circle: {round(areaCircle(radius),2)}")
