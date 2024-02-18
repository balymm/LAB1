#exercise 1: Create a generator that generates the squares of numbers up to some number N.

def squares_generator(N):
    for i in range(1, N + 1):
        yield i**2

N = int(input())
squares = squares_generator(N)

for square in squares:
    print(square)

""""
exercise 2: Write a program using generator to print the even numbers between 0 and n in comma separated 
form where n is input from console.
"""

def evens_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())

evens = evens_generator(n)

for even in evens:
    print(even)

"""
exercise 3: Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, 
between a given range 0 and n.
"""

def divisible_generator(n):
    for i in range(n + 1):
        if i % 12 == 0:
            yield i

n = int(input())

divisible = divisible_generator(n)

for divides in divisible:
    print(divides)


"""
Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" 
loop and print each of the yielded values.
"""

def squares_generator(a, b):
    for i in range(a, b + 1):
        yield i**2

a = int(input())
b = int(input())

square = squares_generator(a, b)

for squares in square:
    print(squares)


#exercise 5: Implement a generator that returns all numbers from (n) down to 0.


def down_zero_generator(n):
    for i in range(n, n - n - 1, -1):
        yield i

n = int(input())
to_zero = down_zero_generator(n)

for zeros in to_zero:
    print(zeros)