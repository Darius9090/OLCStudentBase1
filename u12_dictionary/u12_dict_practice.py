# # 2. Practice Exercises
# menu={"hamburger":6,
#       "fries":5,
#       "pizza":15,
#       "coke":2}
# pizzaprice=menu["pizza"]
# print(f"the price of pizza is {pizzaprice}")
# menu["hotdog"]=9
# print(menu)
# menu["hotdog"]=10
# print(menu)
# choice=input("what do u want to eat?")
# if choice in menu:
#     print(f"Yes,{choice} is in menu")
#     print(f"Give me ${menu[choice]}")

# print(f"welcome to my restaurant")
# print("here is my menu")
# for food,choice in menu.items():

#     print(f'{food}:${choice}')
# for food in menu:
#     print(food)
#     print(menu[food])


# pre exercise for max number in a list algorithm
list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]
maxnum=0
for i in list1:
    if i>maxnum:
        maxnum=i
print(maxnum)


###########################################################
# Part 2. IN-CLASS Practice Exercises

# In-Class Exercise 1: Student Grades Analysis
# Scenario: A teacher needs to analyze student performance.
# Create a dictionary with student names as keys and grades as values.
students = {
    'Ali': 88, 'Benny': 75, 'Chloe': 92, 'Diana': 85,
    'Ethan': 78, 'Farid': 81, 'Grace': 66, 'Haziq': 94,
    'Ivy': 71, 'Jun': 88, 'Ullas':45, 'Josephine':98,
    'Sor Lang': 23, 'Jimmy': 5, 'Borui': 78, 'Esther': 9}

# # Task 1: Identify and print the name of the highest scoring student.
studentsscore=0
studentsname=''
for name,score in students.items():
    if score>studentsscore:
        studentsscore=score
        studentsname=name
print(f"The number of students who scored is {studentsscore} ")

#------------------------------------------------------------
# Task 2: Calculate and display the number of students scoring above 80 and their names
studentscount=0
for name,score in students.items():
    if score>80:
        studentscount+=1
        # print the name here
        print(f"{name} passed")
print(f"The number of students who passed is {studentscount}, with {name} passing")


#------------------------------------------------------------
# Task 3: Update all grades by adding 5 points as a bonus.
