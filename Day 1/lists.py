list1=['rose',15,'tulip',7]
list2=['jasmine',5,'sun flower',12,2025]
# list1.append(99)
# list2.insert(3,19)
list1.extend(list2)
# list1.insert(4,2025)
print(list1)
# list1.remove(19)
# list1.pop(4)
# for i in range(len(list1)):
#     print(list1[i])
# [print(x) for x in list1]
# newlist=[x for x in list1 if "e" in x]
# print(newlist)

# if '19' not in list1:
#     print(f"'No' 19 is not in list1")
# print(list1)
# print(list1[-1])
# print(type(list1))
# listdemo=list(('naruto','family guy',2025))
# print(listdemo)
list1copy=list(list1)
print(list1copy)