"""
Exercise 2: Write a Python program to check for access to a specified path. Test the existence,
readability, writability and executability of the specified path
"""

import os
path = r"C:\Users\baurs\Desktop\pp2\lab1"
print(f"Test for existence: {os.access(path, os.F_OK)}\nTest for readability: {os.access(path, os.R_OK)}")
print(f"Test for writability: {os.access(path, os.W_OK)}\nTest for executability: {os.access(path, os.X_OK)}")


#now for non-existent path

path1 = r"C:\Users\baurs\Desktop\pp2\lab10"
print(f"Test for existence: {os.access(path1, os.F_OK)}\nTest for readability: {os.access(path1, os.R_OK)}")
print(f"Test for writability: {os.access(path1, os.W_OK)}\nTest for executability: {os.access(path1, os.X_OK)}")