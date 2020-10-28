# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:24:47 2020

@author: walsh
"""
#Exercise 1
#Let’s say you’ve just finished eating at a restaurant and treated a friend to lunch. Calculate the total that you must pay given the following information. What was the cost of the tip alone?
#Salad: $3.99
#Burger: $12.99
#Wings: $13.99
#Fries: $3.50

#Tax: 10%
#Tip: 15% (In this situation, the tip must be applied to the after-tax cost of the food).

x = 3.99 + 12.99 + 13.99 + 3.5 
y = 0.1 * x
Tip = 0.15 * (x + y)
Total = Tip + x + y
print(Tip)
print(Total)


#Exercise 2
#You’ve been given a secret message, but all of the words are separated, concatenate the strings to piece together the message.

item = "laptop"
action = "buy the"
name = "Armando"
verb = "says"
print(' '.join([name, verb, action, item]))



#Exercise 3
#You’re at a party and need to share 10 pies amongst 4 people. How much should each person receive? If we can only provide full pies, how much would be left over?

Pies = 10
People = 4
Leftovers = Pies % People

print(Leftovers)