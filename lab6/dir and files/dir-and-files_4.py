#Exercise 4: Write a Python program to count the number of lines in a text file.

import os

with open('c:/Users/baurs/Desktop/pp2/helloooo/aoao.txt', 'r') as text:
    x = sum(1 for line in text)
print(x)