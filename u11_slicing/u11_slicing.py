# Exercise 7: Extracting Middle Elements from a List
# Scenario: Extract the middle 3 elements from a list with an odd 
# number of elements.
numbers = [10, 20, 30, 40, 50]
#[start: stop: step]


new_num=numbers[2:5]
print(new_num)
mid=len(numbers)//2

# print(numbers[mid + 1 ] ) # pulling out an item from the list

print(numbers[mid+1])
print(numbers[mid])
print(numbers[mid-1])

