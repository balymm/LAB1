"""
Exercise 3: Write a Python program to test whether a given path exists or not. If the path exist find the 
filename and directory portion of the given path.
"""

import os

path = r"C:\Users\baurs\Desktop\pp2\helloooo"

if os.path.exists(path) == True:
    print(f"Directory name:{os.path.dirname(path)}")
    print(f"Files in this Directory: {os.path.basename(path)}")
else:
    print("You have zero!")