
#--------------------------------------------------
# WAP to check if a list is palindrome or not
#--------------------------------------------------

# list1 = [1,2,1]

# copy_list1 = list1.copy()
# copy_list1.reverse()
# if(copy_list1 == list1): 
#     print("PALINDROME")
# else :
#     print("NOT A PALINDROME")


#--------------------------------------------------
# WAP to print sum of n natural numbers (using while)
#--------------------------------------------------

# i = 1
# sum=0
# n=int(input("n :"))
# while i<=n:
#     sum = sum + i
#     i = i+1
# print(sum)

# or

# for val in range(1,n+1):
#     sum += val
# print(sum)


#--------------------------------------------------
# WAP to find factorial of first n numbers (using for)
#--------------------------------------------------

# fact = 1
# n=int(input("n :"))
# for i in range (1, n+1):
#     fact = fact * i
# print("factorial of", n , "is" , fact)

#--------------------------------------------------
# WAP to find factorial of first n numbers (using function)
#--------------------------------------------------

# def calc_fact (n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)
    
# calc_fact(5)

#--------------------------------------------------
# WAP to convert USD to INR (using function)
#--------------------------------------------------

# def usd_inr(usd_val):
#     inr_val = usd_val*83
#     print(usd_val,"USD = ", inr_val, "INR")

# usd_inr(10)
    
#--------------------------------------------------
# WAP to find factorial of first n numbers (using recursion)
#--------------------------------------------------

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * fact(n-1)

# print(fact(4))

#--------------------------------------------------
# WAP to print sum of n natural numbers (using recursion)
#--------------------------------------------------

# def sum(n):
#   if(n==1):
#     return 1
#   else:
#     return n + sum(n-1)
  
# print(sum(5))


#--------------------------------------------------
# WAP to print all elm in a list (using recursion)
#--------------------------------------------------

# def print_list(list,idx = 0):
#   if(idx == len(list)):
#     return
#   print(list[idx])
#   print_list(list,idx+1)

# fruits = ["apple", "cherry", "banana"]
# print_list(fruits)

#------------------------------------------------------
# oops practice
#-------------------------------------------------------
# 1. avg of 3 subject marks

# class student:

#   def __init__(self, name , marks):
#     self.name = name
#     self.marks = marks 
    

#   def avg(self):
#    sum = 0
#    for value in self.marks:
#      sum += value
#    print ("hi", self.name, "your avg score is:", sum/3)

# s1 = student("rishi", [78,98,89])
# s1.avg()







