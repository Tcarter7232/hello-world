Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> width = float(input("Enter the width"))
Enter the width4
>>> length = float(input("Enter the length"))
Enter the length11
>>> area = width * lenght
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    area = width * lenght
NameError: name 'lenght' is not defined. Did you mean: 'length'?
>>> area = width * length
>>> print("The area is" , area, "square units.")
The area is 44.0 square units.
>>> width - float(input("Enter the width"))
Enter the width15
-11.0
>>> length = int(input("Enter the length"))
Enter the length8
>>> area = width * length
>>> print("The area is" , area, "square units.")
The area is 32.0 square units.
>>> width = float(input("Enter the width"))
Enter the width8
>>> length = float(input("Enter the length"))
Enter the length8
>>> area = width * height
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    area = width * height
NameError: name 'height' is not defined
>>> area = width * length
>>> print("The area is". area, "square units.")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print("The area is". area, "square units.")
AttributeError: 'str' object has no attribute 'area'
>>> print("The area is" , area, "square units.")
The area is 64.0 square units.
