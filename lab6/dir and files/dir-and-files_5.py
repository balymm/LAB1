#Exercise 5: Write a Python program to write a list to a file.

import os
list = list(input().split())
with open('example file.txt', 'w') as file:
    for i in list:
        file.write(str(i) + ' ')

