# numbers = [1, 2, 3, 4, 3, 2, 1]
# print(numbers)
# index = numbers.index(3,1,6)

# print(f"The index of 3 between positions 2 and 5 is: {index}")

list1=[2,3,1,5,9,7,6,4]


list1.append(8)

add=[10,12]
list1.extend(add)
print(list1)

list1.insert(5,11)
print(list1)

# list1.remove(9)
# print(list1)

index9=list1.index(9,2,6)
print(f"Index of '9' in between index 2 to 6 is : { index9 }" )
list1.append(10)


list1.append(9)
count9=list1.count(9)
print(f"Count of '9' in the list is : {count9}")

list1.sort()
list1.remove(12)
print(list1)

list1.pop(6)
print(list1)
