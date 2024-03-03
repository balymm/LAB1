#Exercise 1: Write a Python program to list only directories, files and all directories, files in a specified path.

import os

for root, directories, files in os.walk(r"C:\Users\baurs\Desktop\pp2\lab1"):
    print(root)
    for directory in directories:
        print(directory)
    for file in files:
        print(file)

        
