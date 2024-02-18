import math

#exercise 1: Write a Python program to convert degree to radian.

degree = int(input())

print(math.radians(degree))


#exercise 2: Write a Python program to calculate the area of a trapezoid.

import math

height, base1, base2 = int(input()), int(input()), int(input())

Area = 1/2 * height * (base1 + base2)

print(Area)


#exercise 3: Write a Python program to calculate the area of regular polygon.

import math

number_of_sides, length_of_side = int(input()), int(input())

Area = number_of_sides * length_of_side**2 / (4 * math.tan(math.radians(180 / number_of_sides)))

print(Area)


#exercise 4: Write a Python program to calculate the area of a parallelogram.

import math

base, height = int(input()), int(input())

print(float(base * height))



