Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mass = float(input("Enter the mass of the object in kilograms:")
...              25
...              
SyntaxError: '(' was never closed
>>> mass = float(input('Enter the mass of the object in kilograms: '))
...              
Enter the mass of the object in kilograms: 85
>>> velocity = float(input("Enter the velocity of the object in meters per second:"))
...              
Enter the velocity of the object in meters per second:119
>>> momentum = mass * velocity
...              
>>> print("The momentum of the object is:", momentum)
...              
The momentum of the object is: 10115.0
