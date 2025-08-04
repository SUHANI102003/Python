"""
#--------------------------------------------------
#                    OUTPUT
#--------------------------------------------------
print("hello world")   #automatically inserts a new line
print("my age is 22")
print("my name is suhani.", "my age is 22")  #will print in same line
print(23)  # can print without double quotes
print(23+8)

#--------------------------------------------------
#                    VARIABLES
#--------------------------------------------------
name = "suhani"
age = 23
price = 34.2
print ("name") # will print name
#to print value
print(name)
print(age)
print ("My name is :", name )
print ("My age is :", age)

# Assignment Rule
# LHS assigned to RHS

age2 = age
print (age2)  #23 ;as 23 was stored in age

#--------------------------------------------------
#                    DATA TYPES
#--------------------------------------------------
print(type(name))   #str - string
print(type(age))    #int
print(type(price))  #float

# can also write string in these ways also
name1 = 'suhani'
name2 = '''sj'''
print(name1)
print(name2)

age1 = 23
old = False  # F is capital
a = None
print(type(old))  # bool
print(type(a))    # NoneType

#--------------------------------------------------
#                    SUM OF 2 NUMBERS
#--------------------------------------------------
a = 2
b = 5
sum = a+b
print(sum)
# or
print(a+b)

#--------------------------------------------------
#                    INPUT FROM USER
#--------------------------------------------------

#string
name = input("name :")
print(name)

#integer
age = int(input("age is :"))
print(age)
print("My name is", name, "and my age is", age)

#float
price = float(input("price is :"))
print(price)

#--------------------------------------------------
#                    OPERATORS
#--------------------------------------------------
# arithmetic

a = 5
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)   #  int/int gives float
print(a**b)  # exponent
print(a%b)   # remainder

# relational / comparision
# will return True / False
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)

# assignment 
num = 10
num = num + 10
# num += 10
# num -= 10
# num *= 10
# num /= 10
# num %= 10
# num **= 10
print("num : ", num)

#logical
# returns boolean value
print (not False)
print (not True)
print (not (a>b))

val1 = True
val2 = True
print("and operator :", val1 and val2)
print("or operator :", val1 or val2)
print("or operator :", (a==b) or (a>b))


#--------------------------------------------------
#               TYPE CONVERSION
#--------------------------------------------------
a = 2
b = 4.25

sum = a + b  # 2.0 + 4.25
print(sum)   # 6.25

c = "2"
d = 4.25
print(c+d) #error can only concatenate str (not "float") to str
"""

#--------------------------------------------------
#               TYPE CASTING
#--------------------------------------------------
c = int("2")
d = 4.25
print(c+d)

a = 3.14
a = str(a)
print(type(a))




