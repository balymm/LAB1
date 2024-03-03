"""
#Exercise 8: Write a Python program to delete file by specified path. Before deleting check for
access and whether a given path exists or not.
"""

import os

path="A.txt"
def delete_path(path):
    if not os.path.exists(path):
        print("Path does not exist")
        return 0
    os.remove(path)
    print("Deleted")

delete_path(path)