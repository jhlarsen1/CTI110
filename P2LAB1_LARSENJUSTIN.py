# Justin Larsen
# 10/1/20224
# P2LAB1
# Using built in libraries for math calculations


import math


# Get float(radius) from user
pi = math.pi

circ_radius = float(input("What is the radius of the circle? "))
print()


# Calculate/Display Diameter of the circle
circ_diameter = (2 * circ_radius)

print(f"The diameter of the circle is {circ_diameter:.1f}")
print()


# Calculate/Display Circumfrence of the circle
circumf = (2 * pi * circ_radius)

print(f"The circumfrence of the circle is {circumf:.2f}")
print()


# Calculate/Display area of the circlce
circ_area = (pi * circ_radius ** 2)
print(f"The area of the circle is {circ_area:.3f}")
print()





