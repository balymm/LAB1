#Exercise 7: Write a Python program to copy the contents of a file to another file

import os
with open('example file.txt', 'r') as r:
    with open('example_file_copy.txt', 'w') as w:
        for line in r:
            w.write(line)