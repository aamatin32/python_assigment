##Quadrant Identifier: Write a Python program that takes the coordinates (x, y) of
#a point as input and prints out which quadrant it belongs to (1st, 2nd, 3rd, or 4th).

x=int(input("Enter x axis: "))
y=int(input("Enter y axis: "))


if x>0 and y>0:
    quadrant_identifier = '1st'
elif x<0 and y>0:
    quadrant_identifier = '2nd'
elif x>0 and y<0:
    quadrant_identifier = '3rd'
else:
    quadrant_identifier = '4th'

print("Entered coordinates (",x,",",y,")","is in: ", quadrant_identifier, "quadrant")