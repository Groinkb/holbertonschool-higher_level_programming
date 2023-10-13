#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(my_square.__dict__)
print(type(my_square))

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
