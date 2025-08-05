#----------------------------------------------------
#                      FUNCTIONS
#-----------------------------------------------------

# a = 5 
# b = 10
# sum = a+b
# print(sum)

# more lines of code

# a = 12
# b=4
# sum = a+b
# print(sum)

# more lines of code

# a = 12
# b=5
# sum = a+b
# print(sum)

# code keeps getting repeat or redundant

## therefore create a function to perform the task of sum

#-----------------------------------------------------
# declaring and defining function

# def calc_sum(a,b):  # function definition
#     sum = a + b
#     print(sum)
#     return sum


# calling function
# calc_sum(2,4)  # arguements
# calc_sum(2,10)
# calc_sum(4,4)

# did not have to write code again & again 

#----------------------------------------------------
#function definition
# def calc_sum(a,b):  #parameters
#     return a+b

# sum = calc_sum(1,2) # function call; arguments
# print(sum)

#--------------------------------------------------
# def print_hello():  # no parameters and return value
#     print("hello")

# output = print_hello()
# print(output)  # None as function does not return anything

#-----------------------------------------------------

# average of 3 numbers

# def avg(a,b,c):
#   return (a+b+c)/3

# print(avg(1,2,3))

#--------------------------------------------------
# in -built functions

# print("suhani","jain") # will give space automatically
# will automatically print in next line
# print("suhani")
# if we do not want next line ->

# print("suhani", end=" ") # sep = " "
# print("jain")

#--------------------------------------------------
# default parameters
# def cal_prod(a,b):
#     print(a*b)
#     return a*b

# cal_prod()  #no arguements  ## error  -cal_prod() missing 2 required positional arguments: 'a' and 'b'

#--------------------------------------------
# def cal_prod(a = 2,b = 5):   # default values of a,b
#     print(a*b)
#     return a*b

# cal_prod()  # no error

#--------------------------------------------
# def cal_prod(a ,b = 5):   # default values of a,b
#     print(a*b)
#     return a*b

# cal_prod(1)  # no error

#--------------------------------------------
# def cal_prod(a = 2,b ):   # default values of a,b
#     print(a*b)
#     return a*b

# cal_prod(2)  # error as Non-default argument follows default argument


#------------------------------------------------------
# function to print length of list
# cities = ["delhi", "gurgaon", "noida", "pune"]
# heroes = ["thor", "ironman", "shaktiman"]

# def print_list(list):
#     print(len(list))

# print_list(cities)
# print_list(heroes)

# function to print elements of list in single line

# print(heroes[0])
# print(heroes[1])
# ## will print in next line S0,
# print(heroes[0], end=" ")
# print(heroes[1], end=" ")


#function
# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(heroes)


#----------------------------------------------------
#                   RECURSION
#-----------------------------------------------------

# def show(n):
#     print(n)

# show(5)  
# now i want to print 5, 4, 3, 2, 1 in one function call only ---> can use loop BUT we'll do by recursion

# def show(n):
#     if(n==0):      # base case - stopping condition
#         return
#     print(n)
#     show(n-1)
#     print("end")

# show (5)

#-------------------------------------------------------










