# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:24:38 2020

@author: walsh
"""
#Define a function called yell that takes in a string and returns a new string that is capitalized and ends in an exclamation mark.

#Example:

#test_1 = yell("hello world")
#print(test_1)
# "HELLO WORLD!"

def yell(phrase):
    string = phrase
    Allcaps = string.upper() + "!"
    return Allcaps
yell("hello world")



#Define a function called is_palindrome that takes a string, and returns True if the string is a palindrome. A palindrome is a string of characters that can be read forward and backward with no change to the meaning.

#Example:

#test_1 = is_palindrome("racecar")
#print(test_1)
 # True

#test_2 = is_palindrome("hello world")
#print(test_2)
# False

def is_palindrome(phrase):
    string1 = phrase
    string2 = string1[::-1]
    if (string2 == string1):
        print("True")
    else:
        print("False")
    

test_1 = is_palindrome("racecar")
print(test_1)


test_2 = is_palindrome("hello world")
print(test_2)


L1 = [5, 1, 3]
L2 = []

def fill_zero(L, n):
    for lists in range(len(L), n):
        L.append(0)
        
fill_zero(L1, 5)
print(L1)
    
fill_zero(L2, 6)
print(L2)



def is_prime(n):
    x = 2
    y = True
    while(n > x):
        y = y and n % x != 0
        x += 1
    return y
            
            
            
        
test = is_prime(29)   
print(test)