#exercise 1:

class String:
    def __init__(do):
        do.string = ""
    
    def getString(do):
        do.string = input("Enter smth")
        return do.string
    
    def printString(do):
        return do.string.upper()
    
test = String()
print(test.getString())
print(test.printString())



#exercise 2 and 3 (because oni svyazany):

class Shape:

    def __init__(do):
        do.ar = 0

    def area(do):
        return do.ar
    
class Square(Shape):
    def __init__(do, length):
        super().__init__()
        do.length = length
        do.ar = length * length

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width * 2

s1 = Square(12)
print(s1.area())
s2 = Rectangle(2, 3)
print(s2.area())



#exercise 4:

import math

class Point:

    def __init__(do, x, y):
        do.x = x
        do.y = y

    def Show(do):
        print(f"x = {do.x}, y = {do.y}")

    def Move(do, z, w):
        do.x = z
        do.y = w
        return do

    def Dist(do, p):
        print(math.sqrt((p.x - do.x) ** 2 + (p.y - do.y) ** 2))


t1 = Point(3, 4)
t2 = Point(5, 6)

t2.Show()

t3 = t1.Move(1, 2)
t2.Dist(t1)
t3.Show()



#exercise 5:

class Account:
    
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough")
        else:
            self.balance -= amount
            return self
        

#exercise 6:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(list(filter(lambda x: all(x % i != 0 for i in range(2, int(x))) and x != 1, arr)))

    