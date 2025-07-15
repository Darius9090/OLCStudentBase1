# ###################################################
# # Part 1: Learning Exercises

# # Exercise 1: Converting to Uppercase
# # Write a program to convert a string to uppercase.
# # Example: Input = "hello", Output = "HELLO".
# word = "hello"
# word = word.upper() # convert to upper case
# print(word)

# # change to lower case .lower()
# print("WORLD".lower())

# # check if an input is all upper case
# # .isupper()

# # code = input("Type a code. Must be upper case: ")
# # if code.isupper():
# #     print(f"{code} is valid")
# # else:
# #     print(f"{code} is not valid")


# # Exercise 10: Validating Uppercase Input
# # Scenario: You are entering product codes into a system, and 
# # all codes must be in uppercase letters (e.g., "ABC123").
# # ask again and again until the user types in all upper case


# # while code.islower:
# #     print("That is not valid")
# #     code=input("please input in a code: ")
    
# while True:
#     code=input("Please insert a sentence: ")
#     if code.isupper():
#         print("That is a valid sentence")
#         break
#     else:
#         print("That is invalid")
    

# #------------------------------------------------------------
# # Exercise 11: Validating Alphanumeric Input
# # Scenario: A username field only accepts alphanumeric characters
# # (letters and numbers) without special symbols.
# # .isalnum()
# while True:
#     username=input("Please input a username")
#     if username.isalnum():
#         print("That is a valid username")
#         break
#     else:
#         print("That is invalid")

#------------------------------------------------------------
# Exercise 12: Validating Numeric Input
# Scenario: You are collecting a phone number that must contain 
# only numeric characters.
while True:
    phone_num=input("please input in a phone number: ")
    if phone_num.isdigit():
        print("New phone number")
        break
    else:
        print("invalid")

