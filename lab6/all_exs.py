#Exercise 1: Write a Python program with builtin function to multiply all the numbers in a list

numbers = [5, 3, 2, 6]

#print(numbers[0] * (sum(numbers[1:])+1))


"""
Exercise 2: Write a Python program with builtin function that accepts a string and calculate the number
of upper case letters and lower case letters
"""

some_string = "BAlymSEkenova"
upper = sum(map(lambda x : x.isupper(), some_string))
lower = sum(map(lambda x : x.islower(), some_string))

#print(upper, lower)


#Exercise 3: Write a Python program with builtin function that checks whether a passed string is palindrome or not.

#string_input = input()
#print(string_input == string_input[::-1])


#Exercise 4: Write a Python program that invoke square root function after specific milliseconds

import time
import math

#num = int(input("Sample input: "))
#ms = int(input("ms: "))
#time.sleep(ms / 1000)
#print(f"Square root of {num} after {ms} milliseconds is {math.sqrt(num)}")

#Exercise 5: Write a Python program with builtin function that returns True if all elements of the tuple are true.

tuple1 = [True, 1 ,545, True]
tuple2 = [True, 1 ,545, True, 0]
#print(all(tuple1))
#print(all(tuple2))



#sorry for everything being in hashtags, every exercise need some prints(

