# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 15:20:08 2020

@author: walsh
"""
#Exercise 1
#Perform the following operations on the list below:

#number_list = [120, 230, 340, 450, 560]

#Print the list in reverse order.
#Add the next number in the sequence to the list.
#Remove the middle value. In its place add a number half of its value.

number_list = [120, 230, 340, 450, 560]

print(number_list[::-1])

number_list.append(670)
print(number_list)
number_list.pop(2)
number_list.insert(2, 170)
print(number_list)


#Exercise 2
#You’ve left your home to head to work, and the following dictionary is an example of what you might have with you. Perform the following operations on the dictionary listed below.
#Add a key to everyday_carry called 'pocket'.
#Set the value of 'pocket' to be a list consisting of the strings 'coins', 'keys', 'wireless headphones', and ‘lip balm’.
#Because we’ve spent some money on a cup of coffee, remove 'coins' from pocket.
#Now that we’ve arrived at work, remove 'laptop' from bag.
#Packing up for lunch, add 'laptop' back to bag, and also add 'papers' to bag.


everyday_carry = {
    'money' : 50,
    'bag' : ['laptop', 'phone charger', 'wallet'],
    'lunchbox' : ['salad','fork', 'soup','spoon','crackers']
}

x = ['coins', 'keys', 'wireless headphones', 'lip balm']
everyday_carry['pocket'] = x
print(everyday_carry)
everyday_carry['pocket'].remove('coins')
everyday_carry['bag'].remove('laptop')
everyday_carry['bag'].append('laptop')
everyday_carry['bag'].append('papers')



print(everyday_carry)


#Going grocery shopping, perform the following operations on the dictionary listed below:
#Sort the vegetables list.
#Add a new key to our grocery_list called 'carbs'.
#Set the value of 'carbs' to bread and potatoes.
#Remove 'cucumber' and instead, replace it with 'zucchini'.
    
grocery_list = {   
    'vegetables' : ['spinach', 'carrots', 'kale','cucumber', 'broccoli'],
    'meat' : ['bbq chicken','ground beef', 'salmon',]
}

grocery_list['vegetables'].sort()
print(grocery_list)

grocery_list['carbs'] = ('bread', 'potatoes')
print(grocery_list)

grocery_list['vegetables'].remove('cucumber')
grocery_list['vegetables'].append('zucchini')
print(grocery_list)
