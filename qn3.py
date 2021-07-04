'''Write a Python program to guess a number between 1 to 9.'''
import random
a,b=random.randint(1,9),0
while a!=b:
    b=int(input("enter 1to9 "))
print("well guessed")