
############################################################
# Part 1: Learning Exercises 
# input() and and .format()

# Exercise 1: Using input() for Text
# Write a program to ask the user for their favorite color and display it.
# Example: If the user enters "blue", the program should display
# "Your favorite color is blue."




#------------------------------------------------------------
# Exercise 2: Understanding input() Behavior
# Write a program to ask the user for their age and display it.
# Example: If the user enters "15", display "Your age is 15."
# Note: Treat the input as a string for now.
# age=input("what is your present age? ")
# print("your current age is "+ age)
# num1=int(input("what is your first number "))
# num2=int(input("whazt is your second number "))
# answer=num1 +num2
# print(f"{num1}+{num2}={answer}")


#------------------------------------------------------------
# Exercise 3: Comparing String Formatting Methods
# Write a program to ask the user for their name and age and display it
# in three different ways. Example: Input name = "John", age = 15




#------------------------------------------------------------
# Exercise 4: Formatting a Message with .format()
# Write a program to display a sentence about favorite subjects.
# Example: Input subject = "Math", reason = "exciting"


#------------------------------------------------------------
# Exercise 5: Comparing .format() and f-strings for a Calculation
# Write a program to calculate the sum of two numbers and format the
# output in two ways: using .format() and f-strings.




#######################
# len() function - measures how long/ how many items something is

# word = "AUSTRALIA"
# word_length=len(word
)
# print(word_length)

# fruits = ["apple", "orange", "watermelon", "mango","rambutan", "durian","grapes","banana"]
# fruits_length=len(fruits)
# print(f"the amount of fruits is {fruits_length}")

uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = "abcdefghijklmnopqrstuvwxyz"
nums = "0123456789"
specials = "!@#$%^&*()"

import random
print(uppers[random.randint(1, len(uppers))])