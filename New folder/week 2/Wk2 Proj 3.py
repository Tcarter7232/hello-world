Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> radius = float(input("Enter the radius of the sphere:"))
Enter the radius of the sphere:16
>>> diameter = 2 * radius
>>> circumference = diameter * math.pi
>>> surface_area = 4 * math.pi * radius**2
>>> volume = (4/3) * math.pi * radius**3
>>> print("Radius =", radius)
Radius = 16.0
>>> print("Diameter:", diameter)
Diameter: 32.0
>>> print("circumference:", circumference)
circumference: 100.53096491487338
>>> print("Surface area:", surface_area)
Surface area: 3216.990877275948
>>> print("Volume:", volume)
Volume: 17157.284678805056
