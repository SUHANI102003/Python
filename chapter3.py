#-----------------------------------------------------
#                 LISTS AND TUPLES
#------------------------------------------------------

# marks1 = 67.2
# marks2 = 66.5
# marks3 = 98.6
# marks4 = 79.3

# too many variables

# DO THIS INSTEAD  -> CREATE A LIST
"""
marks = [67.2, 66.5, 98.6, 79.3]
print(marks)
print(type(marks))

print(len(marks))
print(marks[3])

# in python list we can have multiple data types

student = ["suhani", 98, "Delhi"]
print(student)
print(student[2])

# can modify list (cannot in string)

student[0] = "arjun"
print(student)

#-----------------------------------------------------
# LIST SLICING
#-----------------------------------------------------
# negative index exists too

marks1 = [65, 78, 56, 34, 89]
print(marks[1:])
print(marks[-3:-2])

#-----------------------------------------------------
# LIST METHODS
#-----------------------------------------------------

list = [2,1,3]
list1 = ["apple", "berry", "grape"]
# print(list.append(4))  ## returns none

list.append(4)
print(list)

list.sort() # ascending
print(list)

list.sort(reverse=True)   # descending
print(list)

list1.sort()
print(list1)

list.reverse()
print(list)

list.insert(3,5)
print(list)

list3 = [2,1,3,1]

list3.remove(1) # removes 1st occurance of elm
print(list3)

list3.pop(2)  # 2 is index
print(list3)
"""

#-----------------------------------------------------
#                    TUPLES
#-----------------------------------------------------

tup = (2,1,3,1)

print(tup[1])

#tup[0] = 5 # error not allowed
#'tuple' object does not support item assignment

tup1 = ()  #empty tuple
print(tup1)  

tup2 = (1)  # will be considered as a normal integer surronded by parenthesis
print(tup2)  # ignored brackets
print(type(tup2))  # int

# tup2 = (1,)  now it will be tupple , so add a comma

print(tup[1:3])

#-------------------------------------------------------
#   TUPPLE METHODS
#-------------------------------------------------------

print(tup.index(1))  # 1
print(tup.count(1))  # 2