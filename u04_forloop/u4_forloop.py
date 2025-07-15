# write a cheer program for someone
# name=input("Give me a name ")
# for char in name:
#     print(f"Give me a {char}")
# print(f"{name} is the best")


# ###################################################
# # Part 1: Learning Exercises
# # Exercise 1: Simple Loop with range(stop)
# # Write a program to print "Welcome to Python!" 5 times.
# # Use range(stop) to repeat the message.

# for i in range(5):
#     print("hello!")

# # #------------------------------------------------------------
# # # Exercise 2: Printing Numbers with range(stop)
# # # Write a program to print numbers from 0 to 4 using range(stop).
# # # Example: Output = 0, 1, 2, 3, 4.
# # for i in range(5):  # Loop from 0 to 4
# #     print("Number: {}".format(i))
# for i in range(100):
#     print("Number: {}".format(i))

# # #------------------------------------------------------------
# # # Exercise 3: Counting with range(start, stop)
# # # Write a program to print numbers from 10 to 15.
# # # Use range(start, stop) to set the range.
# # # Example: Output = 10, 11, 12, 13, 14, 15.
# for i in range(10, 16):  # Loop from 10 to 15
#     print("Counting: {}".format(i))

# # count from 21 to 29
# for i in range(21,30):
#     print("Counting:{}".format(i))


# # #------------------------------------------------------------
# # # Exercise 4: Using range(start, stop, step)
# # # Write a program to print even numbers from 2 to 10.
# # # Use range with a step value.
# # # Example: Output = 2, 4, 6, 8, 10.


# for i in range(2,50,3):
#     print("Value number 3:{}".format(i))


# # #------------------------------------------------------------
# # # Exercise 5: Printing Numbers in Reverse
# # # Write a program to print numbers from 10 to 1.
# # # Use range(start, stop, step) with a negative step value.
# # # Example: Output = 10, 9, 8, ..., 1.
# for i in range(10,0,-1):
#      print("Countdown: {}".format(i))


# # #------------------------------------------------------------
# # # Exercise 6: Summing Numbers in a Range
# # # Write a program to calculate the sum of numbers from 1 to 10.
# # # Use range(start, stop) and a loop to add the numbers.
# # # Example: Output = 55.
# # total = 0
# for i in range(1, 11 ):  # Loop from 1 to 10
   
#     i+=1
# print("The total sum is: {}".format(i))


# # #------------------------------------------------------------
# # # Exercise 7: Printing a Simple Pattern
# # # Write a program to print the following pattern:
# # # *
# # # **
# # # ***
# # # ****
# # # *****
# for i in range(1, 6):  
#      print("*" * i)






# ###########################################################
# # Part 2. IN-CLASS Practice Exercises

# # Exercise 8: Printing Odd Numbers
# # Write a program to print all odd numbers from 1 to 15.
# # Use range(start, stop, step) to skip even numbers.
# # Example: Output = 1, 3, 5, ..., 15.
# # range(start, stop, step)

# for i in range(1, 16, 2):   # 1, 3, 5, 7, 9, 11, 13, 15
#     print(i)


# #------------------------------------------------------------
# # Exercise 9: Multiplying Numbers
# # Write a program to print the first 5 multiples of 7.
# # Use range(start, stop, step).
# # Example: Output = 7, 14, 21, 28, 35.
# for i in range(7 , 36 , 7):
#     print(i)

# #------------------------------------------------------------
# # Exercise 10: Repeating a Phrase
# # Write a program to print "I love Python!" 3 times.
# # Use range(stop) to repeat the phrase.
# for i in range(3):
#     print("I love python!")


# #------------------------------------------------------------
# # Exercise 11: Custom Counting Pattern
# # Write a program to print the following pattern:
# # 5
# # 44
# # 333
# # 2222
# # 11111
# print("1"*5) # 11111

#  # Loop for rows
# print("5"*1)
# print("4"*2)
# print("3"*3)
# print("2"*4)
# print("1"*5)



# #------------------------------------------------------------
# # Exercise 12: Generating a Multiplication Table
# # Write a program to print the multiplication table of 6.
# # Example: 6 x 1 = 6, ..., 6 x 10 = 60.
# for i in range(1 , 11, 1):
#     # 6 x 1 = 6
#     print("6 x " + str(i) + " = " + str(6 * i)) 
    




# #------------------------------------------------------------
# # Exercise 13: Printing a Custom Star Pattern
# # Write a program to print the following pattern:
# # *
# # ***
# # *****
# # *******
# # *********
# for i in range(1, 10 , 2):  
#      print("*" * i)


# using for loops

# # print numbers from 0 - 9
# for i in range(10):
#     print(i)

# # print numbers from 1 to 15
# for i in range(1,16):
#     print(i)

# # print even numbers from 2 to 24
# for i in range(2,25,2):
#     print(i)

# print numbers from 10 to 1
# range(start, stop, step)
for i in range(10,0,-1):
    print(i)