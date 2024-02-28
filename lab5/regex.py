import re

file = open("C:/Users/baurs/Desktop/pp2/lab5/row.txt")
list_file = file.readlines()

#Exercise 1: Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

file = open("C:/Users/baurs/Desktop/pp2/lab5/row.txt")
list_file = file.readlines()

def a_b():
    for word in list_file:
        if len(re.findall("ab*", word)) != 0:
            print(word, " -> ", end="")
            print(re.findall("ab*", word))

#a_b()



#Exercise 2: Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

file = open("C:/Users/baurs/Desktop/pp2/lab5/row.txt")
list_file = file.readlines()

def a_bb():
    for word in list_file:
        if len(re.findall("ab?b{2}", word)) != 0:
            print(word, " -> ", end="")
            print(re.findall("ab?b{2}", word))

#a_bb()
            

#exercise 3: Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

file = open("C:/Users/baurs/Desktop/pp2/lab5/row.txt")
list_file = file.readlines()

def lower():
    for word in list_file:
        if len(re.findall("[a-z]*_+", word)) != 0:
            print(word, " -> ", end="")
            print(re.findall("[a-z]*_+", word))

#lower()
            
#Exercise 4: Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

file = open("C:/Users/baurs/Desktop/pp2/lab5/row.txt")
list_file = file.readlines()

def up_low():
    for word in list_file:
        if len(re.findall('([A-Z{1}a-z*])', word)) != 0:
            print(word, " -> ", end="")
            print(re.findall('^([A-Z{1}a-z*])-?$'))

#up_low()
            

#Exercise 5: Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

file = open("C:/Users/baurs/Desktop/pp2/lab5/row.txt")
list_file = file.readlines()

def a_tob():
    for word in list_file:
        if len(re.findall("a.*b", word)) != 0:
            print(word, " -> ", end="")
            print(re.findall("a.*b", word))

#a_tob()
            

#Exercise 6: Write a Python program to replace all occurrences of space, comma, or dot with a colon.
            
import re

file = open("C:/Users/baurs/Desktop/pp2/lab5/row.txt")
list_file = file.readlines()

def replace():
    for word in list_file:
        if len(re.findall("[ ,.]", word)) != 0:
            print(word, " -> ", end="")
            print(re.sub("[ ,.]", ":", word))

#replace()
            

#Exercise 7: Write a python program to convert snake case string to camel case string.
            
import re

file = open("C:/Users/baurs/Desktop/pp2/lab5/row.txt")
list_file = file.readlines()

def snake_to_camel_case():
    for word in list_file:
        if len(re.findall("_", word)) != 0:
            print(word, " -> ", end="")
            print(re.sub("_", " ", word).title().replace(" ", ""))

#snake_to_camel_case()
            

#Exercise 8: Write a Python program to split a string at uppercase letters.
            
import re

file = open("C:/Users/baurs/Desktop/pp2/lab5/row.txt")
list_file = file.readlines()

def uppercase():
    for word in list_file:
        if len(re.findall("[A-Z]", word)) != 0:
            print(word, " -> ", end="")
            print(re.split("A-Z", word))

#uppercase()


#Exercise 9: Write a Python program to insert spaces between words starting with capital letters.
            
import re

file = open("C:/Users/baurs/Desktop/pp2/lab5/row.txt")
list_file = file.readlines()

def spaces():
    for word in list_file:
        if len(re.findall("ab*", word)) != 0:
            print(word, " -> ", end="")
            lst = re.findall("[A-Z][^A-Z]*", word)
            txt = ""
            for word1 in lst:
                txt += (word1 + " ")

#spaces()

#Exercise 10:
                
import re

file = open("C:/Users/baurs/Desktop/pp2/lab5/row.txt")
list_file = file.readlines()

def camel_to_snake_case():
    for word in list_file:
        if len(re.findall("ab*", word)) != 0:
            print(word, " -> ", end="")
            lst = re.findall("[A-Z][^A-Z]*", word)
            txt = ""
            for i in range(len(lst)):
                if i != len(lst) - 1:
                    txt += lst[i].lower() + "_"
                else:
                    txt += lst[i].lower()

            print(txt)

camel_to_snake_case()


