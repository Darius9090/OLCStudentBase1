import random

# random,randint(1,100) # wrong
num1= random.randint(1, 100)  # random(1,100) # wrong
num2= random.randint(1, 100)# random(1,100) # wrong
if num1 >= num2:
    print(f"{num1} is bigger than {num2}")
else:
    print("false")

#######################################################################
#------------------------------------------------------------
# Exercise 11: Age-Based Group Assignment
# Write a program to categorize a person into groups based 
# on age: Child (0-12), Teen (13-19), Adult (20+).
# Example: Input = 15. Output = "Teen."

import random

numpersons = int(input("How many persons: "))

for i in range(numpersons):
    person=random.randint(1,100) #88
    if person<=12:
        print("child")
    elif person <= 19:
    # if person in range(13,19):
        print("teen")
    # if person>=20:
    else:
        print("adult")


# score = 83

# if score > 95:
#     print('A1')
# if score > 90:
#     print('A2')
# if score > 85:
#     print('C3')
# if score > 80:
#     print('C4')
# if score > 75:
#     print('D5')
# else:
#     print("F")


#------------------------------------------------------------
# Exercise 12: Grade Checker
# Write a program to assign a grade based on marks:
# >= 90: A, >= 75: B, >= 60: C, < 60: D.
# Example: Input = 85. Output = "Grade B."

