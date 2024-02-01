#exercise 1:

def func():
    ounces = int(input())
    grams = 28.3495231 * ounces
    print(grams)

func()


#exercise 2:

def func():
    F = input()
    C = (5 / 9) * (F - 32)
    print(C)

func()


#exercise 3:

def solve(numheads, numlegs):
    initial = numheads
    while numlegs / 2 != numheads:
        numlegs = numlegs - 4
        numheads = numheads - 1
    print({initial - numheads}, {numheads})

solve(35, 94)


#exercise 4:

def primes(lst):
    i = 0
    while i < len(lst):
        removed = False
        for j in range(2, lst[i]):
            if lst[i] % j == 0:
                lst.remove(lst[i])
                removed = True
                break
        if not removed:
            i += 1
    print(lst)
primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])


#exercise 5:

from itertools import permutations

def permutat(string):
    arr = permutations(string)
    for i in list(arr):
        print(i)

permutat("Balym")


#exercise 6:

def string_reverse(string):
    lst = string.split(" ")
    lst = reversed(lst)
    for i in lst:
        print(i, end = " ")

string_reverse("We are ready")


#exercise 7:

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3:
            if nums[i + 1] == 3:
                print(True)
                return True
    print(False)
    return False

has_33([1, 3, 1, 3])


#exercise 8:

def spy_game(nums):
    counter = 0
    for i in range(len(nums)):
        if counter == 1 or counter == 0:
            if nums[i] == 0:
               counter += 1
        elif counter == 2:
            if nums[i] == 7:
                print(True)
                return True
    print(False)
    return False

spy_game([1,0,2,4,0,5,7])


#exercise 9:

import math

def volume(radius):
    print((radius ** 3) * ((4 * math.pi) / 3))
    return (radius ** 3) * ((4 * math.pi) / 3)

volume(3)


#exercise 10:

def unique_el(lst):
    sorte = sorted(lst)
    end = [sorte[0]]
    for i in range(1, len(lst)):
        if sorte[i] != sorte[i - 1]:
            end.append(sorte[i])
    print(end)

unique_el([1, 2, 2, 3])


#exercise 11:

def palindrome(string):
    print(string == string[::-1])
    return string == string[::-1]

palindrome("madam")


#exercise 12:

def histo(lst):
    for i in range(len(lst)):
        for j in range(lst[i]):
            print("*", end = "")
        print("")

histo([4, 9, 7])


#exercise 13:

import random

def guess_number():
    print("Hello! What is your name?")
    name =  input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    secret_num = random.randint(1, 20)

    attempts = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        attempts = attempts + 1


        if guess == secret_num:
            print(f"Good job, {name}! You guessed my number in {attempts} {'guess' if attempts == 1 else 'guesses'}!")
            break
        elif guess < secret_num:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

if __name__ == "__main__":
    guess_number()
    

    