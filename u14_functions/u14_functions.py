# def greeting(yourname, myname):
#     print(f"Hello, {myname} is {yourname}")


# def areatraingle(base,height):
#     area=0.5*base*height
#     print(f"The area of thr triangle is {area}")
    
# areatraingle(34,56)
# areatraingle(90,456)
# areatraingle(87,56)
# areatraingle(4567,56)
# areatraingle(34,3456789)
def cubenumber(number):
    thecube=number*number*number
    return thecube
    
n1 =cubenumber(3)
n2=cubenumber(45)
n3=cubenumber(6)
n4=cubenumber(8)

total = n1 + n2 + n3 + n4
print(total)

# find the cube of 3, 6, 8, 45

# find the sum of all these cubes



# Exercise 1: Random Username Generator
# Write a function that generates a username based on the user's
# first name, last name, a random animal from a list, and a random number.

# List of random animals: ["Tiger", "Lion", "Bear", "Wolf", "Eagle"]
# Random number: Generated between 10 and 99

# Example:
# Input: First Name: "John", Last Name: "Doe"
# Random animal: "Tiger", Random number: 42
# Output: "JohnDoeTiger42"
import random
def genusername(firstname,lastname):
    animals=["Tiger", "Lion", "Bear", "Wolf", "Eagle"]
    ranimals=random.choice(animals)
    ranum=random.randint(1,100)
    uname=firstname + lastname + ranimals + str(ranum)
    return uname
fname=input("what is your first name: ")
lname=input("what is your last name: ")
username=genusername(fname,lname)
print(f"hello {fname}, ur username is {username}")
