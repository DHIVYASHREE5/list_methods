fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

# get the index of 'banana'
index = fruits.index('banana')
print(index)

# 'grapes' is inserted at index 3 (4th position)
fruits.insert(3, 'grapes')
print('List:', fruits)

# remove the element at index 2
removed_element = fruits.pop(2)
print('Removed Element:', removed_element)

# reverse the order of list elements
fruits.reverse()
print('Reversed List:', fruits)

# sort the list
fruits.sort()
print(fruits)

# copying a list
x = fruits.copy()
print(fruits)

#count
x = fruits.count("apple")
print(fruits)

#extend
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print('List after extend():', cars)

# remove banana from the list
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

#clear
fruits.clear()
print(fruits)




