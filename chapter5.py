#----------------------------------------------------
#                       LOOPS
#----------------------------------------------------

#----------------------------------------------------
#                       WHILE LOOP
#               iterator , stopping condition
#----------------------------------------------------

# while(True):
#     print("hello")  # infinite loop 

# count = 1
# while(count <= 5):
#     print("hello")
#     count += 1
# print (count)


# print 1 to 100
# i = 1
# while i<=100:
#     print(i)
#     i += 1


# print 100 to 1
# i = 100
# while i>=1:
#     print(i)
#     i -= 1


# print multiplication table
# i = 1
# n = int(input("enter n :"))
# while i<=10:
#     print(i*n)
#     i += 1

#print elm of list using loop
# traverse
# i = 0
# list = [1,4,9,16,25,36,49,64,81,100]
# while i<len(list):
#     print(list[i])
#     i += 1


#search for a num x in tuple using loop
# tup = (1,4,9,16,25,36,49,64,81,100)
# i = 0
# x = 36
# while i < len(tup):
#   if(tup[i] == x):
#       print("NUM FOUND at index :", i)
#       break
#   else:
#       print("NOT FOUND")
#   i += 1


#break statement
# i=1
# while i<=5:
#   print(i)
#   if(i==3):
#       break
#   i += 1


#continue statement
# i=1
# while i<=5:
#   if(i==3):
#     i += 1
#     continue  # 3 will not print
#   print(i)
#   i += 1

# even values skip , odd print
# i=1
# while i<=10:
#   if(i%2==0):
#     i += 1
#     continue  
#   print(i)
#   i += 1

#----------------------------------------------------
#                      FOR LOOP
#             list, tupple, string traversal
#-----------------------------------------------------

# list
# nums = [1,2,3,4,5]
# for val in nums:
#     print(val)


# tupple
# tup = (1,2,3,4,5)
# for val in tup:
#     print(val)

# string
# str = "suhani"
# for char in str:
#     print(char)


# for with else
# str = "suhani"
# for char in str:
#     if(char == "a"):
#         print("a found")
#     print(char)
# else:
#     print("end")    # acts as a break 


# print elm in list using for loop
# list = [1,4,9,16,25,36,49,64,81,100]

# for val in list:
#     print(val)



#search for a num x in tuple using loop
# tup = (1,4,9,16,25,36,49,64,81,100)
# x = 64
# i = 0
# for el in tup:
#     if(el==x):
#         print(x,"found in tup at index", i)
#         break
#     i += 1
        


#----------------------------------------------------
#                 RANGE FUNCTION
#-----------------------------------------------------

#seq = range(10)
# print(seq[0])
# print(seq[1])
# print(seq[2])

# for i in seq:   # 0 to 9
#     print(i)


# for i in range(2,10):  ## 2 = start , 10 = stop
#     print(i)


# for i in range(2,10,2):  ## 2 = start , 10 = stop , 2 = step size
#     print(i)


# for i in range(2, 100, 2):  # even numbers b/w 2 and 100
#     print(i)

# num = int(input("n:"))
# for i in range(1,11):
#   print(i*num)



#----------------------------------------------------
#                 PASS STATEMENT
#-----------------------------------------------------

# null statement that does nothing

# for i in range(5):
#     #empty (as we do not want to anything)

# print("some useful work")  # gives error


for i in range(5):
    pass
print("some useful work") 